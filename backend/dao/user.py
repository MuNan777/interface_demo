from models.user import User
from db.database import get_db

db = get_db()

class UserDao():
  # get user by id
  def get_user(id):
    return User.query.get(id)
  
  def get_user_by_name(name):
    return User.query.filter(User.name == name).first()

  # get all users
  def get_user_list():
    users = User.query.all()
    return users
  
  # get user page
  def get_user_page(page, pageSize):
    users = User.query.order_by(User.uid.desc()).offset((page - 1) * pageSize).limit(pageSize).all()
    return users

  def get_user_count():
    return User.query.count()

  # create user
  def create_user(user):
    try:
      db.session.add(user)
      db.session.commit()
      return user
    except:
      return None

  # update user
  def update_user(user):
    try:
      db.session.commit()
      return user
    except:
      return None

  # remove user
  def remove_user(user):
    try:
      db.session.delete(user)
      db.session.commit()
      return True
    except:
      return False
    
    