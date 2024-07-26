import json

from flask import jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count



def buy_rate_user(beginTime, endTime):
    try:
        # 创建 Spark 会话，只需在应用启动时创建一次
        spark = SparkSession.builder \
            .appName("Top3 Highest/Lowest Buy-rate Users") \
            .config("spark.executor.instances", "6") \
            .config("spark.executor.memory", "8g") \
            .config("spark.executor.cores", "4") \
            .config("spark.driver.memory", "4g") \
            .config("spark.default.parallelism", "24") \
            .getOrCreate()
        # 读取CSV文件到DataFrame
        df = spark.read.csv("hdfs://master:9000/input/UserBehavior.csv", header=True, inferSchema=True)

        # 计算每个user_id的出现次数
        user_id_count = df.groupBy("user_id").agg(count("*").alias("total_count"))

        # 计算每个用户的购买次数
        user_id_buy_count = df.where(col("action") == "buy") \
            .groupBy("user_id") \
            .agg(count("*").alias("buy_count"))

        # 计算每个用户的购买率，并且只保留最高的三个
        buy_rate_highest_df = user_id_buy_count.join(user_id_count, "user_id") \
            .select("user_id",
                    (col("buy_count") / col("total_count")).alias("buy_rate")) \
            .orderBy(col("buy_rate").desc()) \
            .limit(3)

        # 计算每个用户的购买率，并且只保留最低的三个
        buy_rate_lowest_df = user_id_buy_count.join(user_id_count, "user_id") \
            .select("user_id",
                    (col("buy_count") / col("total_count")).alias("buy_rate")) \
            .orderBy(col("buy_rate").asc()) \
            .limit(3)

        # 将结果转换为 JSON 格式
        highest_results = buy_rate_highest_df.toJSON().collect()
        lowest_results = buy_rate_lowest_df.toJSON().collect()

        # 将 JSON 数据转换为 Flask 可用的格式
        highest_json = [json.loads(row) for row in highest_results]
        lowest_json = [json.loads(row) for row in lowest_results]

        # 把 highest 和 lowest 存进一个大数组里
        result = {"highest": highest_json, "lowest": lowest_json}

    finally:
        # 处理完成后停止 Spark 会话
        spark.stop()

    return jsonify({
        "code": 200,
        "msg": "success",
        "data": result
    })
