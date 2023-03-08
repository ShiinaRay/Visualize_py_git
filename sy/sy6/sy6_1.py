from pyecharts import options as opts
from pyecharts.charts import Pie, Line, Map, Page


def pie_doughnut_chart() -> Pie:
    x_data = ["NBA", "CBA", "国际足球", "中国足球", "步行街", '游戏电竞', '自建模板', '运动装备', '综合体育',
              '虎扑社团', '站务管理']
    y_data = [232345, 16976, 44381, 124, 512266, 129065, 3805, 35124, 4454, 646, 34467]
    c = (
        Pie(init_opts=opts.InitOpts(width="1280px", height="720px"))
        .add(
            series_name="发帖数",
            data_pair=[list(z) for z in zip(x_data, y_data)],
            radius=["50%", "70%"],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(pos_left='left', pos_top='middle', orient="vertical"),
                         title_opts=opts.TitleOpts(title="虎扑社区各板块发帖数"))
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            # label_opts=opts.LabelOpts(formatter="{b}: {c}")
            # label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
            # label_opts=opts.LabelOpts(color="skyblue"),
            label_opts=opts.LabelOpts(),
        )
    )
    return c


def line_markpoint() -> Line:
    x_data = ["0：00", "2：00", "4：00", "6：00", "8：00", '10：00', '12：00', '14：00', '16：00',
              '18：00', '20：00', '22:00']
    y_data1 = [259, 114, 134, 397, 840, 1577, 1413, 713, 647, 448, 462, 514]
    y_data2 = [1221, 370, 359, 845, 2270, 3582, 2947, 2215, 2106, 1843, 2045, 2178]
    c = (
        Line(init_opts=opts.InitOpts(width="1280px", height="720px"))
        .add_xaxis(x_data)
        .add_yaxis(
            "NBA",
            y_data1,
            # markpoint_opts=opts.MarkPointOpts(symbol='circle'),
            symbol="circle",
            symbol_size=15,
        )
        .add_yaxis(
            "虎扑",
            y_data2,
            # markpoint_opts=opts.MarkPointOpts(symbol='diamond'),
            symbol="diamond",
            symbol_size=15,

        )
        .set_global_opts(title_opts=opts.TitleOpts(title="虎扑社区和NBA板块的24小时发帖量"),
                         yaxis_opts=opts.AxisOpts(name="发帖数(个)",
                                                  name_location="middle",
                                                  name_gap=50, ),
                         )
    )
    return c


def map_jiangsu() -> Map:
    MAP_DATA = [
        ["苏州市", 1274], ["南京市", 931], ["徐州市", 908], ["南通市", 772], ["无锡市", 746], ["盐城市", 670],
        ["常州市", 527], ["宿迁市", 498], ["连云港市", 459], ["扬州市", 455], ["淮安市", 455], ["泰州市", 451], ["镇江市", 321],
    ]
    c = (
        Map(init_opts=opts.InitOpts(width="1280px", height="720px"))
        .add(
            series_name="用户量",
            maptype="江苏",
            data_pair=MAP_DATA,
            is_map_symbol_show=False,
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="虎扑社区江苏省用户地域分布",
                subtitle="用户数据来自百度",
                subtitle_link='https://www.baidu.com/',
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b}<br/>{c}"
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=300,
                max_=1300,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],
            ),
        )
    )
    return c


def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout, page_title="虎扑分析", )
    page.add(
        pie_doughnut_chart(),
        line_markpoint(),
        map_jiangsu(),
    )
    page.render("虎扑分析.html")


if __name__ == "__main__":
    page_simple_layout()


