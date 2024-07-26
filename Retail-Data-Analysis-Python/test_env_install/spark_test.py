from pyspark.sql import SparkSession

try:
    # 创建SparkSession
    spark = SparkSession.builder \
        .appName("SparkHDFSAccess") \
        .master("local[*]") \
        .getOrCreate()

    # 读取虚拟机HDFS中的原始数据
    hdfs_url = "hdfs://master:9000/input/UserBehavior.csv"
    df = spark.read.csv(hdfs_url, header=True, inferSchema=True)

    # 显示数据表头
    print("表头：", df.columns)

except Exception as e:
    print(f"读取数据时出错: {e}")

finally:
    # 关闭SparkSession
    spark.stop()
