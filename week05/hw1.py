import redis

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
passwd=conf['passwd']

#redis keys initialization
client = redis.Redis(host=host, password=passwd)
client.hset('video_count', 1001, 1)
client.hset('video_count', 1002, 1)

def counter(video_id: int):   
    client = redis.Redis(host=host, password=passwd)
    count_number = client.hget('video_count', video_id)
    client.hset('video_count', video_id, int(count_number.decode())+1)
    return count_number

if __name__ == '__main__':
    print(counter(1001).decode())
    print(counter(1001).decode())
    print(counter(1002).decode())
    print(counter(1001).decode())
    print(counter(1002).decode())
