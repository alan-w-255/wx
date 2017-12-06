import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'postgresql://wxdbuser:wxpaw-ord@localhost:5432/wxdb'

engine = create_engine(DATABASE_URI) # 创建数据库引擎

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # 在这里导入所有的可能与定义模型有关的模块，这样他们才会合适地
    # 在 metadata 中注册。否则，您将不得不在第一次执行 init_db() 时
    # 先导入他们。
    import models.Model
    Base.metadata.create_all(bind=engine)

def drop_all():
    import models.Model
    Base.metadata.drop_all(bind=engine)
