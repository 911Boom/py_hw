import sqlite3
import pandas as pd
conn = sqlite3.connect('gaokao.db')
c = conn.cursor()
c.execute('select province from prov')
province = c.fetchall()
df = pd.DataFrame(province, columns=['province'])
df.to_csv('province.csv', index=False, encoding='utf-8')