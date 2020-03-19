import csv
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map
from pyecharts.charts import Bar, Page, Pie, Timeline
from pyecharts.charts import Geo

quxian = ['阿城区', '巴彦县', '道里区', '方正县', '木兰县', '南岗区', '尚志市', '双城区', '松北区','五常市','香坊区','道外区']


with open("/Users/maxuan/Desktop/课程/1/python/npc2/harbin2.csv","r",encoding = "utf-8",newline="") as f:
    rows = csv.reader(f)
    tl = Timeline().add_schema(is_auto_play=True,play_interval= 1000)
    for row in rows:
        if(row[0]!=""):
            values = []
            pair = []
            for i in range(3,48,4):
                values.append(int(row[i]))
            for i in range(0,len(quxian)):
                pair.append((quxian[i],values[i]))
            bar=(
               Bar()
               .add_xaxis(quxian)
               .add_yaxis("哈尔滨市各区县确诊人数", values)
               .reversal_axis()
               .set_series_opts(label_opts=opts.LabelOpts(position="right"))
               .set_global_opts(title_opts=opts.TitleOpts(title=row[1]))
            )
            tl.add(bar, "{}".format(row[1]))
        else:
            break
tl.render(path="visBar.html")

