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
html = requests.get(url, headers=headers, data={'lnlqnf': '2021', 'lnlqsheng': 'bj', 'entoken': entoken, 'hash': hash})
print(html.text)
def query(province, year):
    print(province, year)
    payload = {
        'lnlqnf': '2011',
        'lnlqsheng': 'bj',
        'entoken': entoken,
        'hash': hash
    }
    html = requests.get(url, data=payload)
    html.encoding = html.apparent_encoding
    bs = BeautifulSoup(html.text, 'html.parser')
    data = bs.find_all('td')
    l = []
    for item in data:
        if item.text is None:
            continue
        t = 7
        if len(l) > 1 and (l[1].isdigit() or len(l[1]) == 0):
            t = 6
        l.append(item.text)
        if len(l) == t:
            # print(l)
            l = []
        # if t==6:



# # query('吉林', '2022')
html = requests.get('http://zsb.jlu.edu.cn/index/admission.html')
html.encoding = html.apparent_encoding
bs = BeautifulSoup(html.text, 'html.parser')
data = bs.find_all('option')
years = []
provinces = []
for item in data:
    if(item['value'].isdigit()):
        years.append(item['value'])
    else:
        provinces.append(item['value'])

print(years, provinces)


# for year in years:
#     for province in provinces:
#         query(province, year)
