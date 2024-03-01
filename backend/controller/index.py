from controller.user import user

def register_routes(app):
  # 注册蓝图
  app.register_blueprint(user, url_prefix='/api/user')

