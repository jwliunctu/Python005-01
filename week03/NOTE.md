学习笔记

-- 新建資料庫 testdb --
mysql> create database testdb;
Query OK, 1 row affected (0.00 sec)
mysql> show create database testdb;
+----------+-----------------------------------------------------------------------------------------------+
| Database | Create Database                                                                               |
+----------+-----------------------------------------------------------------------------------------------+
| testdb   | CREATE DATABASE `testdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ |
+----------+-----------------------------------------------------------------------------------------------+


-- 新增使用者 --
CREATE USER 'Dj'@'%' IDENTIFIED BY 'password';


-- 使用者權限 --
grant all privileges on *.* to 'Dj'@'%' IDENTIFIED by 'password';



-- 修改字符集 -- 
alter database testdb character set utf8mb4;

-- 是否進行密碼強度驗證 --
set global validate_password_policy = 0 ;