-- 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证，新建一个数据库 testdb，并为该数据库增加远程访问的用。
-- * 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
-- * 将增加远程用户的 SQL 语句作为作业内容提交

-- 版本5.7.32 --
$ mysql -V
mysql  Ver 14.14 Distrib 5.7.32, for Linux (x86_64) using  EditLine wrapper


-- 配置檔案修改字符集 --
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
[client]
 default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4

[mysqld]
character_set_server = utf8mb4
init_connect = 'SET NAMES utf8mb4'
character_set_client_handshake = FALSE
collation_server = utf8mb4_unicode_ci

-- 驗證字符集 --
mysql> show variables LIKE 'character%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+

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
