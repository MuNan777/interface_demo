from flask import Blueprint, jsonify, json, request
from service.user import UserService

# 创建名为 'user' 的蓝图
user = Blueprint('user', __name__)

# 获取用户列表的路由
@user.route('/list', methods=['GET'])
def get_user_list():
    return jsonify(UserService.get_user_list())

# 分页获取用户的路由
@user.route('/page', methods=['GET'])
def get_user_page():
    # 验证请求参数中的页码和每页大小
    result = validate_page(request.args)
    if result:
        return jsonify(result)

    # 获取页码和每页大小参数
    page = request.args.get('page')
    pageSize = request.args.get('pageSize')

    return jsonify(UserService.get_user_page(page, pageSize))

# 根据用户ID获取用户的路由
@user.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return jsonify(UserService.get_user_by_id(user_id))

# 创建用户的路由
@user.route('/', methods=['POST'])
def create_user():
    # 从请求中获取 JSON 数据
    data = request.get_json()

    # 验证用户数据
    result = validate_user(data)
    if result:
        return jsonify(result)

    # 从数据中获取用户姓名和性别
    name = data['name']
    gender = data['gender']

    return jsonify(UserService.create_user(name, gender))

# 更新用户的路由
@user.route('/<int:user_id>', methods=['POST'])
def update_user(user_id):
    # 从请求中获取 JSON 数据
    data = request.get_json()

    # 从数据中获取用户姓名和性别
    name = data['name']
    gender = data['gender']

    return jsonify(UserService.update_user(user_id, name, gender))

# 删除用户的路由
@user.route('/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    return jsonify(UserService.remove_user(user_id))

# 验证分页参数的函数
def validate_page(data):
    if 'page' not in data or not data['page'].isdigit() or int(data['page']) < 0:
        return {'message': 'Invalid page'}
    if 'pageSize' not in data or not data['pageSize'].isdigit() or int(data['pageSize']) < 1:
        return {'message': 'Invalid page'}
    return None

# 验证用户数据的函数
def validate_user(data):
    if 'name' not in data or not (2 <= len(data['name']) <= 20):
        return {'message': 'Invalid name'}

    if 'gender' not in data or not (data['gender'] in [0, 1]):
        return {'message': 'Invalid gender'}
    return None