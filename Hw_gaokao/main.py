import re

import requests
from bs4 import BeautifulSoup
import pandas
import sqlite3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

url = 'http://zsb.jlu.edu.cn/index/admission.html'
rq = requests.get(url, headers=headers)
bs = BeautifulSoup(rq.text, 'html.parser')
form = bs.find('form', id='admission')
entoken1 = re.compile('<input name="entoken" type="hidden" value="(.*?)"/>')
hash1 = re.compile('<input name="hash" type="hidden" value="(.*?)"/>')
entoken = entoken1.findall(str(form))[0]
hash = hash1.findall(str(form))[0]
print(entoken, hash)
conn = sqlite3.connect('gaokao.db')
c = conn.cursor()


def query(province, year):
    print(province, year)
    payload = {
        'lnlqnf': year,
        'lnlqsheng': province,
        'entoken': entoken,
        'hash': hash
    }
    html = requests.post(url, data=payload)
    html.encoding = html.apparent_encoding
    bs = BeautifulSoup(html.text, 'html.parser')
    data = bs.find_all('td')
    l = []
    for item in data:
        if item.text is None:
            continue
        t = 6 if (len(l) > 1 and (l[1].isdigit() or len(l[1]) == 0)) else 7
        l.append(item.text)
        if len(l) == t:
            l = [0 if x == '——' else int(x) if x.isdigit() else x for x in l]
            print(l)
            if t == 6:
                c.execute('insert into gk1 values(?,?,?,?,?,?)',
                          [int(year), province, l[0], l[3], l[4], l[5]])
                conn.commit()
            else:
                c.execute('insert into gaokao values(?,?,?,?,?,?,?,?)',
                          [int(year), province, l[1], l[2], l[4], l[5], l[3], l[6]])
                conn.commit()
            l = []


# # query('吉林', '2022')
html = requests.get(url, headers=headers)
html.encoding = html.apparent_encoding
bs = BeautifulSoup(html.text, 'html.parser')
data = bs.find_all('option')
years = []
provinces = []
for item in data:
    if item['value'].isdigit():
        years.append(item['value'])
    else:
        provinces.append(item['value'])


# query('xz', '2022')

for year in years:
    for province in provinces:
        query(province, year)
