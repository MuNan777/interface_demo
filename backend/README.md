# Backend

Python3 + Flask + SQLAlchemy ORM + Mysql

### 配置 `config\index.py`

```python
# 配置文件
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://xxx:xxx@localhost/py_demo' # 数据库连接字符串，创建 py_demo 数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 启动

```bash
python .\index.py
```



