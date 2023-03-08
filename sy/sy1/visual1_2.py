import numpy as np
import matplotlib.pyplot as plt

x = np.arange(7)
# x = ['FY2013', 'FY2014', 'FY2015', 'FY2016', 'FY2017', 'FY2018', 'FY2019']
y1 = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
bar_width = 0.4
plt.bar(x, y1, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016', 'FY2017', 'FY2018', 'FY2019'], width=bar_width)
# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 设置图片名称
plt.title("2013-2019财年淘宝和天猫平台的GMV")
# 设置x轴标签名  Fiscal Year
plt.xlabel("财年")
# 设置y轴标签名   Gross Merchandise Volume
plt.ylabel("GMV(单位：亿元)")
# 用于给柱状图添加图例（注释）
# plt.legend(['单位：亿元'], loc='upper left')
# 显示
plt.show()
