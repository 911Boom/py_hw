from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import pandas as pd
import re
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import sqlite3
import time

conn = sqlite3.connect('ssq.db')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3880.400 QQBrowser/10.8.4554.400'}

dict = {
    '2023': (2023001, 2023073), '2022': (2022001, 2022150), '2021': (2021001, 2021150), '2020': (2020001, 2020134),
    '2019': (2019001, 2019151), '2018': (2018001, 2018153), '2017': (2017001, 2017154), '2016': (2016119, 2016153)
}

cur = conn.cursor()


def query1(url, x):
    print(url)
    opt = ChromeOptions()
    opt.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get(url)
    # find all the elements with class name 'kjqH'
    ele = []
    elements = driver.find_elements(By.CLASS_NAME, 'kjqH')
    for element in elements:
        ele.append(element.text)
    ele.append(driver.find_element(By.CLASS_NAME, 'kjqL').text)
    eles = driver.find_elements(By.TAG_NAME, 'dd')
    ele.append(eles[-2].text)
    ele.append(driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div[1]/div[2]/span').text)
    ele = ele[6:]
    ele = [x] + ele
    ele[-1] = ele[-1][5:].replace('年', '-').replace('月', '-').replace('日', '')
    driver.quit()
    print(ele)
    cur.execute('insert into ssq values (?,?,?,?,?,?,?,?,?,?)', ele)
    conn.commit()


def query(url, x):
    print(url)
    session = HTMLSession()
    response = session.get(url, headers=headers)
    response.html.render()
    html = response.html.html
    soup = BeautifulSoup(html, 'lxml')
    ele = []
    data = soup.find_all(class_='kjqH')
    for i in data:
        ele.append(i.text)
    ele.append(soup.find(class_='kjqL').text)
    ele.append(re.findall('<dt>一等奖中奖情况：</dt><dd>(.*?)</dd>', html)[0])
    ele.append(soup.find(class_='sj').text)
    ele = ele[6:]
    ele = [x] + ele
    ele[-1] = ele[-1][5:].replace('年', '-').replace('月', '-').replace('日', '')
    print(ele)
    cur.execute('insert into ssq values (?,?,?,?,?,?,?,?,?,?)', ele)
    conn.commit()


start = time.perf_counter()
url = 'https://www.zhcw.com/kjxx/ssq/kjxq/?kjData={}'
for year in range(2017, 2024):
    for x in range(dict[str(year)][0], dict[str(year)][1] + 1):
        if len(cur.execute('select * from ssq where id=?', (x,)).fetchall()) != 0:
            continue
        print(time.perf_counter() - start)
        query(url.format(x), x)
