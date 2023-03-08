import pyecharts.options as opts
from pyecharts.charts import Bar3D
import random
from pyecharts.faker import Faker
# Faker.clock     Faker.week
groups = ["A组", "B组", "C组", "D组", "E组", "F组"]
days = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
data = [(i, j, random.randint(0, 100)) for i in range(6) for j in range(7)]
(
    Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px", page_title="公司部门销售额", ))
    .add(
        series_name="销售额",
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=groups),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=days),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="公司部门销售额"),
        visualmap_opts=opts.VisualMapOpts(
            max_=100,
            range_color=[
                'pink',
                'skyblue',
            ],
        ),
        legend_opts=opts.LegendOpts(inactive_color='skyblue'),

    )
    .render("公司部门销售额.html")
)
