import sqlite3
import matplotlib.pyplot as plt
import pyecharts.options as opts
from pyecharts.charts import Map
import pandas as pd


def get_data(sql_text):
    conn = sqlite3.connect('gaokao.db')
    c = conn.cursor()
    c.execute(sql_text)
    return c.fetchall()


def visual(years, specializeds):
    map = Map().set_global_opts(
        title_opts=opts.TitleOpts(title="高考分数"),
        visualmap_opts=opts.VisualMapOpts(max_=700, min_=400),
    )
    for year in years:
        for specialized in specializeds:
            print(year, specialized)
            sql_text = '''
            select prov.province,gk1.score,gk1.specialized
            from gk1,prov
            where gk1.province=prov.province_sx
            and year = {}
            and specialized = '{}'
            '''.format(year, specialized)
            df = pd.DataFrame(get_data(sql_text), columns=['province', 'score', 'specialized'])
            if df.empty:
                continue
            print(df)
            map.add("{}{}高考分数".format(year, specialized), [list(z) for z in zip(df['province'], df['score'])],
                    "china")

    c = map
    c.render('./map1.html')


years = tuple(range(2021, 2023))
year = 2022
specializeds = get_data('''
select distinct specialized
from gk1
where year in {}
group by specialized
order by count(*) desc
'''.format(years))
# ['理工一批', '文史一批', '物理类一批',
# '历史类一批', '物理学（中外合作办学）',
# '综合', '广播电视编导（文史）', '农学单列（理工）',
# '广播电视编导（理工）', '软件单列（理工）', '西藏汉（理工）',
# '西藏汉（文史）', '西藏民（理工）', '西藏民（文史）',
# '护理单列（理工）', '南疆计划（理工）']
specializeds = [l[0] for l in specializeds]
print(specializeds)
visual(years, specializeds)
