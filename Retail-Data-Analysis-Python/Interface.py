from flask import Flask, request
from flask_cors import CORS
from waitress import serve
from top_10_browsed_products import get_top_10_browsed_products
from user_activity import get_user_activity
from get_quality_users import get_quality_users
from buy_rate_user import buy_rate_user
from buy_rate_product_category import buy_rate_product_category
from search_most_categories_user import search_most_categories_user

# 创建 Flask 应用实例
app = Flask(__name__)
CORS(app)
@app.route('/fanzong_test')
def fanzong_test():
    return "Hello, World!"

@app.route('/products_popularity', methods=['GET'])
def f1():
    begin_time = request.args.get('beginTime')
    end_time = request.args.get('endTime')
    return get_top_10_browsed_products(begin_time, end_time)

@app.route('/user_activity', methods=['GET'])
def f2():
    begin_time = request.args.get('beginTime')
    end_time = request.args.get('endTime')
    return get_user_activity(begin_time, end_time)

@app.route('/quality_users', methods=['GET'])
def f3():
    begin_time = request.args.get('beginTime') or '2021-01-01'
    end_time = request.args.get('endTime') or '2021-01-01'
    return get_quality_users(begin_time, end_time)

@app.route('/users_buy_rate', methods=['GET'])
def f4():
    begin_time = request.args.get('beginTime') or '2021-01-01'
    end_time = request.args.get('endTime') or '2021-01-01'
    return buy_rate_user(begin_time, end_time)

@app.route('/buy_rate_product_category', methods=['GET'])
def f5():
    begin_time = request.args.get('beginTime') or '2021-01-01'
    end_time = request.args.get('endTime') or '2021-01-01'
    return buy_rate_product_category(begin_time, end_time)

@app.route('/most_categories_user', methods=['GET'])
def f6():
    begin_time = request.args.get('beginTime') or '2021-01-01'
    end_time = request.args.get('endTime') or '2021-01-01'
    return search_most_categories_user(begin_time, end_time)

# 入口点
if __name__ == '__main__':
    print("Flask 服务器正在运行...")
    serve(app, host='127.0.0.1', port=5000)
