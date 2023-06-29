import sqlite3

conn = sqlite3.connect('ssq.db')
cur = conn.cursor()

sql_text = '''
    create table if not exists ssq(
    id integer primary key autoincrement,
    red1 integer,
    red2 integer,
    red3 integer,
    red4 integer,
    red5 integer,
    red6 integer,
    blue integer,
    data text,
    date date
    )
'''
cur.execute(sql_text)
conn.commit()
conn.close()
