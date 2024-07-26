from flask import Flask, jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

def get_quality_users(beginTime, endTime):


    try:
        # 创建 Spark 会话
        spark = SparkSession.builder \
            .appName("Top20 Quality Users") \
            .config("spark.executor.instances", "6") \
            .config("spark.executor.memory", "8g") \
            .config("spark.executor.cores", "4") \
            .config("spark.driver.memory", "4g") \
            .config("spark.default.parallelism", "24") \
            .getOrCreate()
        # 读取CSV文件到DataFrame
        df = spark.read.csv("hdfs://master:9000/input/UserBehavior.csv", header=True, inferSchema=True)

        # 计算每个user的buy次数
        user_counts = df.filter(col("action") == "buy").groupBy("user_id").agg(count("*").alias("count"))

        # 获取出现次数前20的用户
        top_20_users = user_counts.orderBy(col("count").desc()).limit(20)
        bottom_20_users = user_counts.orderBy(col("count").asc()).limit(20)

        # 将Spark DataFrame转换为Pandas DataFrame
        top_20_users_pd = top_20_users.toPandas()
        bottom_20_users_pd = bottom_20_users.toPandas()

        # 将数据转换为JSON格式
        result1 = top_20_users_pd.to_dict(orient="records")
        result2 = bottom_20_users_pd.to_dict(orient="records")

    finally:
        # 处理完成后停止 Spark 会话
        spark.stop()

    return jsonify({
        "code": 200,
        "msg": "success",
        "data":[result1, result2]
    })
