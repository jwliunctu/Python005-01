# 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
#  * 用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
#  * 将 ORM、插入、查询语句作为作业内容提交

import pymysql
from sqlalchemy import create_engine,Table,MetaData,Column,Integer,String,ForeignKey,SmallInteger,DateTime,Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
user=conf['user']
passwd=conf['passwd']
db_name=conf['db_name']

# start ORM
Base = declarative_base()

class User_table(Base): 
    __tablename__ = 'user_orm' 
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=False)
    age = Column(SmallInteger())
    birthday = Column(Date())
    gender = Column(String(5))
    education = Column(String(20))
    created_at = Column(DateTime(),default=datetime.now)
    updated_at = Column(DateTime(),default=datetime.now,onupdate=datetime.now)


# 实例一个引擎
dburl=f"mysql+pymysql://{user}:{passwd}@{host}:3306/{db_name}?charset=utf8mb4"
engine=create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

# INSERT 3 rows by pymysql
db = pymysql.connect(host,user, passwd, db_name)
try:
    sql = '''INSERT INTO user_orm (name, age, birthday, gender, education, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
    values = (
        ('白雅玲', 40, '1980-07-31', '女', '學士', datetime.now(), datetime.now()),
        ('陳宗年', 10, '2010-08-14', '男','國小', datetime.now(), datetime.now()),
        ('鄭夢如', 30, '1990-01-20', '女','博士', datetime.now(), datetime.now())
    )
    with db.cursor() as cursor:
        cursor.executemany(sql, values)
    db.commit()
except Exception as e:
    print(f'INERTT error: {e}')

# SELECT BY pymysql
try:
    sql = '''SELECT name, age, birthday, gender, education FROM user_orm'''
    #sql = '''SELECT COUNT(1) FROM user_orm'''
    with db.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
    db.commit()
except Exception as e:
    print(f'SELECT error: {e}')
finally:
    db.close()