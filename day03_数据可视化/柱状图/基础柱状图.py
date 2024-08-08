import json
from pyecharts.charts import Bar, Line
from pyecharts.options import *

bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar.reversal_axis()

bar.render("基础柱状图.html")
