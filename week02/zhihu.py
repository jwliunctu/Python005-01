import requests
from lxml import etree

url = "https://www.zhihu.com/question/267703735/answer/1610758595"  
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
r = requests.get(url, headers=header)

selector = etree.HTML(r.text)
answer_chunk = selector.xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div[1]/span')
status=r.status_code

if status != 200: pass

with open("answer.txt", "w") as r:
    for line in answer_chunk:
        r.write(line)