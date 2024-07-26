import json

from flask import jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count




def buy_rate_product_category(beginTime, endTime):
    try:
        # 创建 Spark 会话，只需在应用启动时创建一次
        spark = SparkSession.builder \
        .appName("Top3 Bought Products") \
        .config("spark.executor.instances", "6") \
        .config("spark.executor.memory", "8g") \
        .config("spark.executor.cores", "4") \
        .config("spark.driver.memory", "4g") \
        .config("spark.default.parallelism", "24") \
        .getOrCreate()
        # 读取CSV文件到DataFrame
        df = spark.read.csv("hdfs://master:9000/input/UserBehavior.csv", header=True, inferSchema=True)

        # 计算每个product_category的出现次数
        product_category_count = df.groupBy("product_category").agg(count("*").alias("total_count"))

        # 计算每类商品的购买次数
        product_category_buy_count = df.where(col("action") == "buy") \
            .groupBy("product_category") \
            .agg(count("*").alias("buy_count"))

        # 计算每类商品的购买率，并且只保留前三个
        buy_rate_df = product_category_buy_count.join(product_category_count, "product_category") \
            .select("product_category",
                    (col("buy_count") / col("total_count")).alias("buy_rate")) \
            .orderBy(col("buy_rate").desc()) \
            .limit(3)

        # 将 Spark DataFrame 转换为 JSON 格式
        result = buy_rate_df.toJSON().collect()

        # 将 JSON 数据转换为 Flask 可用的格式
        json_result = [json.loads(row) for row in result]
    finally:
        spark.stop()

    return jsonify({
        "code": 200,
        "message": "success",
        "data": json_result
    })

