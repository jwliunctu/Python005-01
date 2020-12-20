
import requests
from lxml import etree
from pathlib import Path
import json
import re


p = Path(__file__)
base_path = p.resolve().parent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def get_page(url, page):
    comments = []
    # 翻頁
    for x in range(page):
        link=f'{url}&start={x*20}'
        p = requests.get(link, headers=headers)
        print(link)

        html = etree.HTML(p.text)
        
        #目標欄位
        author=html.xpath('//*[@id="comments"]/div/div[2]/h3/span[2]/a/text()')
        comment = html.xpath('//div[@class="comment-item "]/div[@class="comment"]/p/span/text()')
        created_at = html.xpath('//div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[@class="comment-time "]/@title')
        star = html.xpath('//div[@class="comment-item "]/div[@class="comment"]/h3/span[@class="comment-info"]/span[contains(@class, "rating")]/@class')

        for idx, content in enumerate(comment):
            try:
                s = re.match("allstar([1-5])0 rating",star[idx])[1]
            except Exception as e:
                s = 0
                print(e)
            print(author[idx],content,created_at[idx],s)
            d = dict(
                author = author[idx],
                star = s,
                content = content,
                created_at = created_at[idx]
            )
            comments.append(d)
    #print(comments)
    with open(base_path.joinpath('data.json'), 'w') as ff:
        ff.write(json.dumps(comments))


if __name__ == '__main__':
    get_page('https://movie.douban.com/subject/1889243/comments?sort=new_score&status=P', 10)
    #get_page('https://movie.douban.com/subject/1889243/comments?sort=time&status=P', 10)
