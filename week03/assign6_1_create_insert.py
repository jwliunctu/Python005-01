#!/usr/bin/python3

# 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

# * 请合理设计三张表的字段类型和表结构；
# * 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
 
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
user=conf['user']
passwd=conf['passwd']
db_name=conf['db_name']

# CREATE TABLE BY ORM
Base = declarative_base()

class Bank_user_table(Base): # 使用者
    __tablename__ = 'bank_user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(20),nullable=False)

class Bank_money_table(Base): # 存款
    __tablename__ = 'bank_money'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,nullable=False)
    money = Column(Float,nullable=False)

class Bank_trans_table(Base): # 轉賬記錄
    __tablename__ = 'bank_trans' 
    id = Column(Integer,primary_key=True)
    from_user_id = Column(Integer,nullable=False)
    to_user_id = Column(Integer,nullable=False)
    money = Column(Float,nullable=False)
    time = Column(DateTime(),default=datetime.now)

# 实例一个引擎
dburl=f"mysql+pymysql://{user}:{passwd}@{host}:3306/{db_name}?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)


# ADD users
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 創建使用者(張三與李四)，各有1000元存款
session.add(Bank_user_table(user_name='張三'))
session.add(Bank_user_table(user_name='李四'))

user = session.query(Bank_user_table.id).filter(Bank_user_table.user_name=='張三').first()
session.add(Bank_money_table(user_id=user.id, money=1000.00))

user = session.query(Bank_user_table.id).filter(Bank_user_table.user_name=='李四').first()
session.add(Bank_money_table(user_id=user.id, money=1000.00))

session.commit()