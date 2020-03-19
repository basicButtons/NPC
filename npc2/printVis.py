import csv
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map
from pyecharts.charts import Bar, Page, Pie, Timeline

from pyecharts.charts import Geo


quxian = ['阿城区', '巴彦县', '道里区', '方正县','木兰县', '南岗区', '尚志市', '双城区', '松北区','五常市','香坊区','道外区','呼兰区','宾县','延寿县','通河县','依兰县']


with open("/Users/maxuan/Desktop/课程/1/python/npc2/harbin2.csv","r",encoding = "utf-8",newline="") as f:
    rows = csv.reader(f)
    tl = Timeline().add_schema(is_auto_play=True,play_interval= 1000)
    for row in rows:
        if (row[0]!=""):
            values = []
            pair = []
            for i in range(3,68,4):
                values.append(int(row[i]))
            for i in range(0,len(quxian)):
                pair.append((quxian[i],values[i]))
                
            map0 = (
                Map()
                .add(
                    "哈尔滨市各地区累计确诊人数",
                    pair,
                    "哈尔滨"
                )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                    title_opts=opts.TitleOpts(title=row[1]),
                    visualmap_opts=opts.VisualMapOpts(max_=30),
                )
            )
            tl.add(map0, "{}".format(row[1]))
        else:
            break
tl.render(path="visF2.html")

