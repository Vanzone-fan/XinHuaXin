from flask import Flask, jsonify
from waitress import serve

# 创建 Flask 应用实例
app = Flask(__name__)

@app.route('/most_browsed_product')
def home():
    return jsonify({"message": "Hello, World!"})

# 入口点
if __name__ == '__main__':
    print("Starting Flask server...")
    # 如果你直接运行这个脚本，将启动 Waitress 服务器
    serve(app, host='0.0.0.0', port=8080)
