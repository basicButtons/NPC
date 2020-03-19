import csv
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map
from pyecharts.charts import Bar, Page, Pie, Timeline

from pyecharts.charts import Geo


quxian = ['阿城区', '巴彦县', '道里区', '方正县', '兰西县', '木兰县', '南岗区', '尚志市', '双城区', '松北区','五常市','香坊区']


with open("/Users/maxuan/Desktop/课程/1/python/npc2/harbin.csv","r",encoding = "utf-8",newline="") as f:
    rows = csv.reader(f)
    tl = Timeline()
    for row in rows:
        values = []
        pair = []
        for i in range(3,48,4):
            values.append(int(row[i]))
        for i in range(0,len(quxian)):
            pair.append((quxian[i],values[i]))
            
        map0 = (
            Geo()
            .add_schema(maptype="哈尔滨")
            .add(
                "geo",
                pair,
                type_=ChartType.HEATMAP,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(min_=-10,max_=20),
                title_opts=opts.TitleOpts(title="Geo-HeatMap"),
            )
        )
        tl.add(map0, "{}".format(row[1]))
tl.render()

