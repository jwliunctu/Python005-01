import redis
import time

# db config
from dbconfig import read_db_config
conf=read_db_config()
host=conf['host']
passwd=conf['passwd']

#redis keys initialization
client = redis.Redis(host=host, password=passwd)

def sendsms(telephone_number, content, limit=5):
    # 短信发送逻辑, 作业中可以使用 print 来代替
    client.set(telephone_number, 0, nx=True, ex=60)
    client.incr(telephone_number)
    if int(client.get(telephone_number)) <= limit:
        print(f'[+] 門號 {telephone_number}， {content} 已成功發送!')
    else:
        print(f'[!] 門號 {telephone_number} 1 分鐘內發送次數超過 5 次, 請等待 1 分鐘')



if __name__ == '__main__':
    print(sendsms(12412512545, content="鬼滅：第一封簡訊"))
    print(sendsms(12412512545, content="鬼滅：第二封簡訊") )   
    print(sendsms(12412512545, content="鬼滅：第三封簡訊") ) 
    print(sendsms(12412512545, content="鬼滅：第四封簡訊"))
    print(sendsms(12412512545, content="鬼滅：第五封簡訊"))
    print(sendsms(12412512545, content="鬼滅：第六封簡訊")) 

    print(sendsms(23236322323, content="老高：第一封簡訊"))
    print(sendsms(23236322323, content="老高：第二封簡訊"))
