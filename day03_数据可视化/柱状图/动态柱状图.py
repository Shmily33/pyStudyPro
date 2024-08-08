from pyecharts.charts import Bar, Line, Timeline
from pyecharts.options import *
from pyecharts.globals import *
# pyecharts为2.0.3版本才不会有x轴数据重叠的bug
f = open("../可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# print(data_lines)
f.close()
# 删除第一行
data_lines.pop(0)
# 将数据转换为字典存储
# { 年份: [ [国家, gdp], [国家,gdp], ......  ], 年份: [ [国家, gdp], [国家,gdp], ......  ], ...... }
# { 1960: [ [美国, 123], [中国,321], ......  ], 1961: [ [美国, 123], [中国,321], ......  ], ...... }
data_dict = {}
# 构造数据
for line in data_lines:
    year = int(line.split(',')[0])
    country = str(line.split(',')[1])
    gdp = float(line.split(',')[2])
    # 判断字典是否为空
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# print(data_dict)

timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份,字典key无须
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8][::-1]  # 取前八倒着排序，这样翻转xy轴就是大的在第一
    # print(year_data)
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])  # 国家
        y_data.append(country_gdp[1] / 100000000)  # gdp

    bar = Bar()
    print(x_data)
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 翻转xy
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据")
    )
    timeline.add(bar, time_point=str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=False,
    is_loop_play=False
)
timeline.render("动态柱状图.html")
