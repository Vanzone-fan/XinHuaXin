from flask import jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

def get_top_10_browsed_products(beginTime,endTime):

    try:
        # 创建 Spark 会话
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

        # 计算每个product_id的出现次数
        product_counts = df.groupBy("product_id").agg(count("*").alias("count"))

        # 获取出现次数前10的产品
        top_10_products = product_counts.orderBy(col("count").desc()).limit(10)

        # 将Spark DataFrame转换为Pandas DataFrame
        top_10_products_pd = top_10_products.toPandas()

        # 将数据转换为JSON格式
        result = top_10_products_pd.to_dict(orient="records")
    finally:
        # 处理完成后停止 Spark 会话
        spark.stop()

    return jsonify({
        "code":200,
        "data":result,
        "msg":"success"
    })


