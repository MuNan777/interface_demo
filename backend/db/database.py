from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# 创建 Flask 应用程序实例
app = Flask(__name__)

# 创建 SQLAlchemy 实例，并使用自定义的 DeclarativeBase 模型基类
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def get_db():
    return db

def init_db():
    import models.user  # 导入用户模型
    db.create_all()  # 创建数据库表结构