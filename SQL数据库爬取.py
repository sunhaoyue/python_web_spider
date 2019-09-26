import os,sys
import requests
import bs4
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='elk',port=3306,charset='utf8')
cur = conn.cursor() #获取指针以操作数据库
#conn.execute('set names utf8')

html = 'https://www.dongmanmanhua.cn/dailySchedule?weekday=MONDAY'
result = requests.get(html)
texts = result.text

data = bs4.BeautifulSoup(texts,'html.parser');
lidata = data.select('div#dailyList ul.daily_card li')
#print(lidata)
arr = {}

for x in lidata:
    did = x.get('data-title-no')
    print(did)
    name = x.select('p.subj')
    name1 = name[0].get_text()
    url = x.a.get('href')
    #print(url)
    story = x.a.p
    story1 = story.string
    user = x.select('p.author')
    user1 = user[0].get_text()
    like = x.select('em.grade_num')
    like1 = like[0].get_text()
    url1="https:"+url
    #print(url+"修改后"+url1)


    cur.execute("INSERT INTO spider(did,name,url,story,user,likes) VALUES(%s, %s,%s,%s,%s,%s)",[did,name1,url1,story1,user1,like1])
    conn.commit()

cur.close()
conn.close()
print("成功！")