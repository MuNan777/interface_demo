from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db.database import get_db, init_db
from controller.index import register_routes
from flask_cors import CORS

app=Flask(__name__)
app.config.from_object('config.index.Config')  # 导入配置信息
db = get_db()
db.init_app(app)

with app.app_context():
    init_db()

register_routes(app)

CORS(app, supports_credentials=True)

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True,port='8000')