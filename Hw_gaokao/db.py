import sqlite3

conn = sqlite3.connect('gaokao.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS gaokao
         (year INT,
            province TEXT,
            specialized TEXT,
            course TEXT,
            max_score INT,
            min_score INT,
            number INT,
            avg_score INT)''')
c.execute('''CREATE TABLE IF NOT EXISTS gk1
        (year INT,
        province TEXT,
        specialized TEXT,
        score INT,
        rank INT,
        score_def INT)''')
conn.commit()