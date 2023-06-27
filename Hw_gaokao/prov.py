import requests
import bs4
import sqlite3

url = 'http://zsb.jlu.edu.cn/index/admission.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
}

html = requests.get(url, headers=headers)
html.encoding = html.apparent_encoding
bs = bs4.BeautifulSoup(html.text, 'html.parser')
# print(html.text)
data = bs.find_all('option')
conn = sqlite3.connect('gaokao.db')
c = conn.cursor()

for item in data:
    if not str(item.text[0]).isdigit():
        c.execute('insert into prov values(?,?)', [item.text, item['value']])
        conn.commit()
