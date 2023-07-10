import requests
from bs4 import BeautifulSoup
import sqlite3
import re

id = '46afb04debb847db0bb07c7ef7a971d1'

conn = sqlite3.connect('zhihu.db')
c = conn.cursor()


def query(id):
    c.execute('select * from zhihu where id = "{}"'.format(id))
    if len(c.fetchall()) > 0:
        return
    url = 'https://www.zhihu.com/people/{}'.format(id)
    print(url)
    headers = {
        'cookie': 'd_c0="ANCYhUhHyxaPTsNEGxLKckldKBW8xjEUY1U=|1684378907"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    html = requests.get(url, headers=headers)
    html.encoding = 'utf-8'
    print(html.text)
    bs = BeautifulSoup(html.text, 'html.parser')
    name = bs.find(class_="ProfileHeader-name")
    if name is None:
        return
    data = [id, name.text]
    dat = bs.find_all(class_="NumberBoard-itemValue")
    for i in dat:
        data.append(i.text)
    t = re.compile('"title":"(.*?)"')
    title = t.findall(html.text)
    data1 = []
    for j in title:
        if len(j) > 0:
            data1.append(j)
    print(data)
    c.execute('insert into zhihu values(?,?,?,?)', data)
    print(data1)
    for k in data1:
        c.execute('insert into zhihu_dynamic values(?,?)', (id, k))
    conn.commit()

# for i in range(10, 100):
#     for j in range(10, 100):
#         t = 'wang-xiu-{}-{}'.format(i, j)
#         query(t)
query('wang-xiu-78-6')
# query('ji-ru-yi-3')
# query('deng-feng-10-87-48')


