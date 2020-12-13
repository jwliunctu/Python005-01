#!/usr/bin/python3

# 张三给李四通过网银转账 100 极客币，现有数据库中三张表：
# 一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
# 第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

# * 请合理设计三张表的字段类型和表结构；
# * 请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

import pymysql
from sqlalchemy import Table, Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dbconfig import read_db_config
import sys

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
user=conf['user']
passwd=conf['passwd']
db_name=conf['db_name']


# start ORM
Base = declarative_base()

class Bank_user_table(Base):
    __tablename__ = 'bank_user'
    id = Column(Integer,primary_key=True)
    user_name = Column(String(20),nullable=False)

class Bank_money_table(Base): 
    __tablename__ = 'bank_money'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,nullable=False)
    money = Column(Float,nullable=False)

class Bank_trans_table(Base): 
    __tablename__ = 'bank_trans' 
    id = Column(Integer,primary_key=True)
    from_user_id = Column(Integer,nullable=False)
    to_user_id = Column(Integer,nullable=False)
    money = Column(Float,nullable=False)
    time = Column(DateTime(),default=datetime.now)

# 实例一个引擎
dburl=f"mysql+pymysql://{user}:{passwd}@{host}:3306/{db_name}?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

# session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 轉帳
session.add(Bank_trans_table(from_user_id=3, to_user_id=4, money=500.0))

# 檢查
query = session.query(Bank_money_table).filter(Bank_money_table.user_id == 3)
money = query.first().money
if money < 500:
    # 回滚
    session.rollback()
else:
    # update
    new_money = money - 500
    query.update({Bank_money_table.money: new_money})
    # 计算接收方新的余额
    query = session.query(Bank_money_table).filter(Bank_money_table.user_id == 4)
    money = query.first().money
    new_balance = money + 500
    query.update({Bank_money_table.money: new_money})

    session.commit()