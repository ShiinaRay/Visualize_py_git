import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Page, Pie

data = pd.read_csv('../pre_data/pre_order.csv', encoding='gbk')

# 畅销前10的商品
def bar_front() -> Bar:
    group = data.groupby(by='商品名称', as_index=False)['总金额(元)'].sum()
    group.sort_values(by='总金额(元)', ascending=False, inplace=True)
    d = group.iloc[: 10]
    x_data = d['商品名称'].values.tolist()
    y_data = np.round(d['总金额(元)'].values, 2).tolist()
    c = (
        Bar(init_opts=opts.InitOpts(width='1080px', height='720px'))
        .add_xaxis(x_data)
        .add_yaxis('', y_data, color='skyblue')
        .set_global_opts(title_opts=opts.TitleOpts(title='畅销前10的商品'),
                         xaxis_opts=opts.AxisOpts(
                             type_='category',
                             axislabel_opts={'interval': '0'}),
                         yaxis_opts=opts.AxisOpts(
                             name='总金额(元)', name_location='center', name_gap=55,),
                         )
    )
    return c

# 滞销后10的商品
def bar_end() -> Grid:
    group = data.groupby(by='商品名称', as_index=False)['总金额(元)'].sum()
    group.sort_values(by='总金额(元)', ascending=False, inplace=True)
    d = group.iloc[-10:]
    x_data = d['商品名称'].values.tolist()
    y_data = np.round(d['总金额(元)'].values, 2).tolist()
    bar = (Bar()
           .add_xaxis(x_data)
           .add_yaxis('', y_data, label_opts=opts.LabelOpts(position='right'), color='pink')
           .set_global_opts(title_opts=opts.TitleOpts(title='滞销后10的商品'),
                            xaxis_opts=opts.AxisOpts(name='总金额(元)', name_location='center',
                                                     name_gap=25, axislabel_opts={'interval': '0'}))
           .reversal_axis()
           )
    grid = Grid(init_opts=opts.InitOpts(width='1080px', height='720px'))
    grid.add(bar, grid_opts=opts.GridOpts(pos_left='10%'))
    return grid

# 销售额与新零售智能销售设备数量的关系
def line_1() -> Line:
    def f(x):
        return len(list(set((x.values))))
    group = data.groupby(by='月份', as_index=False).agg(
        {'设备编号': f, '总金额(元)': np.sum})
    group.columns = ['月份', '设备数量', '销售额']
    c = (
        Line(init_opts=opts.InitOpts(width='1080px', height='720px'))
        .add_xaxis([str(i) for i in group['月份'].values.tolist()])
        .add_yaxis('销售额', np.round(group['销售额'].values.tolist(), 2), color='skyblue',
                   symbol='circle', symbol_size=15)
        .add_yaxis('设备数量', group['设备数量'].values.tolist(), yaxis_index=1, color='pink',
                   symbol='diamond', symbol_size=15)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, position='top', font_size=15))
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(name='月份', name_location='center', name_gap=25),
            title_opts=opts.TitleOpts(title='销售额和新零售智能销售设备数量之间的关系'),
            yaxis_opts=opts.AxisOpts(
                name='销售额（元）', name_location='center', name_gap=70,
                axislabel_opts=opts.LabelOpts(
                    formatter='{value}')))
        .extend_axis(
            yaxis=opts.AxisOpts(
                name='设备数量（台）', name_location='center', name_gap=40,
                axislabel_opts=opts.LabelOpts(
                    formatter='{value}'), interval=50))
    )
    return c

# 用户支付方式饼图
def pie_1() -> Pie:
    group = data.groupby(by='支付状态')['支付状态'].count()
    method = group.index.tolist()
    num = group.values.tolist()
    pie_data = [(i, j) for i, j in zip(method, num)]
    pie = (Pie(init_opts=opts.InitOpts(width='1080px', height='720px'))
           .add('总金额(元)', pie_data, label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'))
           .set_global_opts(title_opts=opts.TitleOpts(title='用户支付方式'),
                            legend_opts=opts.LegendOpts(pos_left='left', pos_top='middle', orient="vertical"),)
           .set_series_opts(
           tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"),
           # label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
           # label_opts=opts.LabelOpts(color="skyblue"),
           label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'),)
           )
    return pie

# 用户所在城市饼图
def pie_2() -> Pie:
    group = data.groupby(by='市')['购买用户'].count()
    cities = group.index.tolist()
    num = group.values.tolist()
    pie_data = [(i, j) for i, j in zip(cities, num)]
    pie = (Pie(init_opts=opts.InitOpts(width='1080px', height='720px'))
           .add('总金额(元)', pie_data, label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'), radius=[100, 200],
                # radius=["50%", "70%"],
                )
           .set_global_opts(title_opts=opts.TitleOpts(title='用户所在城市'))
           .set_series_opts(
           tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"),
           # label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
           # label_opts=opts.LabelOpts(color="skyblue"),
           label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'),)
           )
    return pie

# 用户消费时间段饼图
def pie_3() -> Pie:
    group = data.groupby(by='下单时间段')['购买用户'].count()
    times = group.index.tolist()
    num = group.values.tolist()
    pie_data = [(i, j) for i, j in zip(times, num)]
    pie = (Pie(init_opts=opts.InitOpts(width='1080px', height='720px'))
           .add('总金额(元)', pie_data, label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'),
                radius=[40, 200], rosetype='radius', is_clockwise=False)
           .set_global_opts(title_opts=opts.TitleOpts(title='用户消费时间段'),
                            legend_opts=opts.LegendOpts(pos_right='right', pos_top='middle', orient="vertical"),)
           .set_series_opts(
           tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"),
           # label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
           # label_opts=opts.LabelOpts(color="skyblue"),
           label_opts=opts.LabelOpts(formatter='{b}:{c}({d}%)'),)
           )
    return pie

def page_draggable_layout():
    # page = Page(layout=Page.DraggablePageLayout, page_title='新零售智能销售数据可视化')
    # page.add(
    #     bar_front(),
    #     bar_end(),
    #     line_1(),
    #     pie_1(),
    #     pie_2(),
    #     pie_3(),
    # )
    # page.render("新零售智能销售数据可视化_dev.html")

    Page.save_resize_html("新零售智能销售数据可视化_dev.html", cfg_file="./chart_config.json", dest="新零售智能销售数据可视化.html")


if __name__ == "__main__":
    page_draggable_layout()
