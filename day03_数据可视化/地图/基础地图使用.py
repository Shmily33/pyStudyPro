from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [
    ("重庆市", 5),
    ("上海市", 90),
    ("湖南省", 23),
    ("台湾省", 399),
    ("广东省", 499)
]

map.add("测试地图", data, "china")

map.set_global_opts(visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
        {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
        {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
        {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
    ]
))

map.render("测试地图.html")
