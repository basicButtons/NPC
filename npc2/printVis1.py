import csv/Users/maxuan/Desktop/课程/1/python/npc2
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType
from pyecharts.charts import Map
from pyecharts.charts import Bar, Page, Pie, Timeline,Grid, Line,Scatter


from pyecharts.charts import Geo

bar = (
   Bar()
   .add_xaxis(Faker.choose())
   .add_yaxis("商家A", Faker.values())
   .add_yaxis("商家B", Faker.values())
   .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
)
geo = (
   Geo()
   .add_schema(maptype="china")
   .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
   .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
   .set_global_opts(
       visualmap_opts=opts.VisualMapOpts(),
       title_opts=opts.TitleOpts(title="Grid-Geo-Bar"),
   )
)

grid = (
   Grid()
   .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="95%"))
   .add(geo, grid_opts=opts.GridOpts(pos_left="80%"))
)
print(Faker.choose())
grid.render()
