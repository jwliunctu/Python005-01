# [Mac下安裝和配置Redis](https://www.itread01.com/content/1531505056.html)

# [Debian安裝redis](https://medium.com/一個小小工程師的隨手筆記/在-debian-9-中安裝-redis-並使其成為-service-256da396318f)

```bash
# 下載、解壓縮、編譯 Redis
$ wget http://download.redis.io/redis-stable.tar.gz
$ tar xvzf redis-stable.tar.gz
$ cd redis-stable
$ make

# 嘗試看看是否安裝正確
$ make test
# 報錯You need tcl 8.5 or newer in order to run the Redis test
# 解法 apt-get install tcl

$ make install

# 安裝 Redis Service
./redis-stable/utils/install_server.sh

# Linux安装Redis 6.0.5 ./install_server.sh报错
# 解法: https://www.cnblogs.com/strive-for-life/p/13194306.html
```

設置密碼和bindip: `/etc/redis/6379.conf` 

```bash
requirepass 密碼
bind 0.0.0.0
```

啟動redis server:  `redis-server /etc/redis/6379.conf` 

看server狀態 `ss -ntpl | grep 6379`

關閉server

1. redis-cli
2. auth 密碼
3. shutdown

redis-cli取得key值操作

```bash
if value is of type string -> GET <key>
if value is of type hash -> HGETALL <key>
if value is of type lists -> lrange <key> <start> <end>
if value is of type sets -> smembers <key>
if value is of type sorted sets -> ZRANGEBYSCORE <key> <min> <max>
```

Python安裝redis與連接範例

```python
# pip3 install redis

import redis
cliet = redis.Redis(host='server1', password='password')

```

# 字符串

```python
#把值附加上新的字串
client.set('key', 'value3', nx=True)
client.append('key', 'value4')
result = client.get('key') #result為value3value4

#值的加減
client.set('key2', '100')
result2=client.incr('key2') #101
result3=client.decr('key2') #100

#字符串的數據量級不要超過百萬等級
#不要貿然使用keys * 指令

```

# 列表

```python
#列表插入
client.lpush('list_redis_demo', 'python') #列表左邊插入
client.rpush('list_redis_demo', 'java') #列表右邊插入

#看列表長度
print(client.llen('list_redis_demo')) 

#彈出數據 lpop() rpop()
data = client.lpop('list_redis_demo')
print(data)

#查看一定範圍的列表數據
data = client.lrange('list_redis_demo', 0, -1)
print(data)

#利用列表發送簡訊的範例
while True:
	phone = client.rpop('list_redis_demo')
	if not phone:
		print('發送完畢')
		break
	# sendsms(phone)
	result_items = retry_once(phone)
	if result_items >= 5:
		client.lpush('list_redis_demo', phone)

```

# 集合

跟列表的差別是裡面的值不能重複

```python
#添加值
print(client.sadd('redis_set_demo', 'new_data')) #成功返回1

#隨機取一個數字
client.spop()

#查看所有值
client.snumbers('redis_set_demo')

#交集
client.sinter('set_a','set_b')

#聯集
client.sunion('set_a','set_b')

#差集
client.sdiff('set_a','set_b')

```

# 哈希

```python
#添加VIP用戶
client.hset('vip_user','1001',1)
client.hset('vip_user','1002',1)

#刪除VIP用戶
client.hdel('vip_user','1002')

#檢查用戶是否存在
print(client.hexists('vip_user','1002'))

#添加多個鍵值對
client.hmset('vip_user', {'1003':1,'1004':1})

# hkeys hget hmget hgetall
field = client.hkeys('vip_user')
print(filed)
print(client.hget('vip_user','1001'))
print(client.hgetall('vip_user'))
```

# 有序集合

```python
client.zadd('rank',{'a':4,'b':3,'c':1,'d':2,'e':5})

client.zincrby('rank',-2,'e')

print(client.zrangebyscore('rank',1,5))

#zrevrank 從大到小排

#基card
print(client.zcard('rank'))

#顯示評分
print(client.zrange('rank',0,2,withscores=True))

print(client.zrevrange('rank',0,2,withscores=True))
```

# 重要機制

## 生存時間

定期清除：設定失效時間

惰性清除：定期去檢查

LRU：優先淘汰不是最近使用的數據

LFU：優先淘汰不頻繁使用的數據

## 主從複製

橫向擴展的手段

## 哨兵

監控

通知Notification

自動故障遷移

---

# 消息對列

## 用途

- 異步處理

    範例: 網購結帳

    好處: 減少用戶的等待，提升網站的性能

- 流量控制

    範例: 網購秒殺(令牌生成器)

    100個令牌隊列，拿到令牌就可以購買

- 服務解耦

    上下游的端口與應用整合

## 模型

- 對列模型

    FIFO

- 發佈-訂閱模型

    解決異步處理和服務解耦

## RabbitMQ

是一種RPC

```bash
# 安裝rabbitmq
apt-get install rabbitmq-server
# 開啟插件
rabbitmq-plugins enable rabbitmq_management
#啟動
systemctl start rabbitmq-server
#檢查狀態
ss -ntpl | grep 5672

#新增遠端登入的使用者 https://stackoverflow.com/questions/23669780/rabbitmq-3-3-1-can-not-login-with-guest-guest
rabbitmqctl add_user 帳號 密碼
rabbitmqctl set_user_tags 帳號 administrator
rabbitmqctl set_permissions -p / 帳號 ".*" ".*" ".*"
```