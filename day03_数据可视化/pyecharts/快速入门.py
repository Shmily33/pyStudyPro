from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, TooltipOpts, VisualMapOpts, ToolboxOpts

line = Line()

line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])

# 设置全局配置项set_global_opts
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),  # 标题
    legend_opts=LegendOpts(is_show=True),  # 图例
    toolbox_opts=ToolboxOpts(is_show=True),  # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True),  # 视觉映射
)

# 通过render方法，将代码生成为图像
line.render()
