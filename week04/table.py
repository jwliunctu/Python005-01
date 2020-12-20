#!/usr/bin/python3
 
import pymysql
from sqlalchemy import create_engine,Table,Column,Integer,Float,String,MetaData,ForeignKey,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json
from pathlib import Path

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
user=conf['user']
passwd=conf['passwd']
db_name=conf['db_name']

# CREATE TABLE BY ORM
Base = declarative_base()


class name_table(Base): # 電影評論表
    __tablename__ = 'movie_comment'
    id = Column(Integer,primary_key=True)
    author = Column(String(20),nullable=False)
    star = Column(Integer,nullable=False)
    content = Column(String(1000),nullable=False)
    #created_at = Column(String(100),nullable=False)
    created_at = Column(DateTime(),nullable=False)

# 实例一个引擎
dburl=f"mysql+pymysql://{user}:{passwd}@{host}:3306/{db_name}?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

#讀取json資料
json_file = Path(__file__).resolve().parent.joinpath('data.json')
with open(json_file,'r') as f:
    d=json.loads(f.read())

#寫入資料表
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

for i in d:
    author=i['author']
    content=i['content']
    created_at=datetime.strptime(i['created_at'], "%Y-%m-%d %H:%M:%S")
    star=i['star']

    #print(author, star, content, created_at)

    session.add(name_table(
        author=author,
        star=star,
        content=content,
        created_at=created_at
    ))

session.commit()