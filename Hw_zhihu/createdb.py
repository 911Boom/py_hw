import sqlite3


conn = sqlite3.connect('zhihu.db')
c = conn.cursor()
c.execute('''CREATE TABLE zhihu
         (id text primary key,
name text,
follows_number int,
followers_number int)
            ''')
c.execute('''CREATE TABLE zhihu_dynamic
         (id text,
         title text)
            ''')
conn.commit()
conn.close()
