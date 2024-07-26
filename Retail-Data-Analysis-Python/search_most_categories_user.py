from flask import jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct
import json
import atexit




def search_most_categories_user(beginTime, endTime):
    try:
        # 创建 Spark 会话，只需在应用启动时创建一次
        spark = SparkSession.builder \
            .appName("Top10 Browsed Products") \
            .config("spark.executor.instances", "6") \
            .config("spark.executor.memory", "8g") \
            .config("spark.executor.cores", "4") \
            .config("spark.driver.memory", "4g") \
            .config("spark.default.parallelism", "24") \
            .getOrCreate()

        # 读取CSV文件到DataFrame
        df = spark.read.csv("hdfs://master:9000/input/UserBehavior.csv", header=True, inferSchema=True)

        # 统计每个用户浏览的不同category的products的种类数，只保留前三个
        search_most_user_df = df.select("user_id", "product_category").distinct() \
            .groupBy("user_id") \
            .agg(countDistinct("product_category").alias("unique_product_category_count")) \
            .orderBy(col("unique_product_category_count").desc()) \
            .limit(3)

        # 将 Spark DataFrame 转换为 JSON 格式
        result = search_most_user_df.toJSON().collect()
        result_json = [json.loads(row) for row in result]

    finally:
        # 确保 Spark 会话在异常情况下也能被停止
        spark.stop()

    return jsonify({
        "code":200,
        "msg":"success",
        "data":result_json
    })
