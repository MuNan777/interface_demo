from flask import jsonify, json
from dao.user import UserDao
from models.user import User

class UserService():
  def get_user_by_id(id):
    user = UserDao.get_user(id)
    if user:
      return {
        'errno': 0,
        'message': 'Get user successfully',
        'data': {
          'uid': user.uid,
          'name': user.name,
          'gender': user.gender
        }
      }

  def get_user_list():
    arr = UserDao.get_user_list()
    result = []
    for item in arr:
        result.append({
            'uid': item.uid,
            'name': item.name,
            'gender': item.gender,
        })
    return {
      'errno': 0,
      'message': 'Get user list successfully',
      'list': result
    }
  
  def get_user_page(page, pageSize):
    arr = UserDao.get_user_page(int(page), int(pageSize))
    count = UserDao.get_user_count()
    result = []
    for item in arr:
        result.append({
            'uid': item.uid,
            'name': item.name,
            'gender': item.gender,
        })
    return {
      'errno': 0,
      'message': 'Get user list successfully',
      'list': result,
      'count': count
    }

  def create_user(name, gender):
    user = UserDao.get_user_by_name(name)
    if user:
      return {
        'errno': 1,
        'message': 'User already exists'
      }
    newUser = UserDao.create_user(User(name, gender))
    if newUser:
      return {
        'errno': 0,
        'message': 'Created user successfully',
        'data': {
          'uid': newUser.uid,
          'name': newUser.name,
          'gender': newUser.gender
        }
      }
    else:
      return {
        'errno': 1,
        'message': 'Failed to create user'
      }

  def update_user(id, name, gender):
    user = UserDao.get_user(id)
    if not user:
        return {
          'errno': 1,
          'message': 'User not found'
        }
    
    if user.name != name:
      has = UserDao.get_user_by_name(name)
      if has:
        return {
          'errno': 1,
          'message': 'User already exists'
        }

    if name:
        user.name = name
    if gender is not None:
        user.gender = gender
    newUser = UserDao.update_user(user)
    if newUser:
      return {
        'errno': 0,
        'message': 'Updated user successfully',
        'data': {
          'uid': newUser.uid,
          'name': newUser.name,
          'gender': newUser.gender
        }
      }
    else:
      return {
        'errno': 1,
        'message': 'Failed to update user'
      }

  
  def remove_user(id):
    user = UserDao.get_user(id)
    if user:
      if UserDao.remove_user(user):
        return {
          'errno': 0,
          'message': 'Removed user successfully'
        }
      else:
        return {
          'errno': 1,
          'message': 'Failed to remove user'
        }
    else:
      return {
        'errno': 1,
        'message': 'User not found'
      }
