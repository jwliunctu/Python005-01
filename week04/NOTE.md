# Install pip for Python 3

```bash
$ sudo apt update
$ sudo apt install python3-pip
$ pip3 -V
```

# Install django

```bash
$ pip3 install --upgrade django==2.2.13
$ python3
>>> import django
>>> django.__version__
'2.2.13'
```

# 創建Django專案

```bash
$ django-admin startproject MyDjango
$ find MyDjango
MyDjango/
MyDjango/manage.py #命令行工具
MyDjango/MyDjango
MyDjango/MyDjango/wsgi.py
MyDjango/MyDjango/__init__.py
MyDjango/MyDjango/settings.py #項目配置文件
MyDjango/MyDjango/urls.py
```

# 創建Django應用程序

```bash
$ python3 manage.py help #查看該工具的具體功能
$ python3 manage.py startapp index
$ find index/
index/migrations #數據庫遷移文件夾
**index/models.py #模型**
index/apps.py #當前app配置文件
index/admin.py #管理後台
index/tests.py #自動化測試
**index/views.py #視圖**
```

# 啟動server

```bash
$ python3 manage.py runserver
默認是127.0.0.1:8000

$ python3 manage.py runserver 0.0.0.0:80
```