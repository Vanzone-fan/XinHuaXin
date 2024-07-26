import pymysql
from contextlib import closing

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'vanzone',
    'database': 'retail_analysis'
}

# 创建测试数据库连接
def create_connection():
    return pymysql.connect(**db_config)

# 创建测试表
def create_test_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS test_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL
    )
    """
    with closing(create_connection()) as conn, conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()
        print("测试表创建成功")

# 插入测试数据
def insert_test_data():
    insert_data_query = """
    INSERT INTO test_table (name, age)
    VALUES (%s, %s)
    """
    test_data = [
        ('Alice', 30),
        ('Bob', 25),
        ('Charlie', 35)
    ]
    with closing(create_connection()) as conn, conn.cursor() as cursor:
        cursor.executemany(insert_data_query, test_data)
        conn.commit()
        print("测试数据插入成功")

# 查询并验证数据
def query_and_verify_data():
    query_data_query = "SELECT * FROM test_table"
    with closing(create_connection()) as conn, conn.cursor() as cursor:
        cursor.execute(query_data_query)
        results = cursor.fetchall()
        for row in results:
            print(f"id: {row[0]}, name: {row[1]}, age: {row[2]}")

# 清理测试数据
def cleanup_test_data():
    drop_table_query = "DROP TABLE IF EXISTS test_table"
    with closing(create_connection()) as conn, conn.cursor() as cursor:
        cursor.execute(drop_table_query)
        conn.commit()
        print("测试表删除成功")

# 主函数，执行测试步骤
def main():
    create_test_table()
    insert_test_data()
    query_and_verify_data()
    cleanup_test_data()

if __name__ == "__main__":
    main()
