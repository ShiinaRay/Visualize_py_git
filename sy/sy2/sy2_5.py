import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.arange(7)
# x = ['FY2013', 'FY2014', 'FY2015', 'FY2016', 'FY2017', 'FY2018', 'FY2019']
y1 = np.array([10770, 16780, 24440, 30920, 37670, 48200, 57270])
bar_width = 0.4
# plt.bar(x, y1, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016', 'FY2017', 'FY2018', 'FY2019'], width=bar_width)
bar_rects=plt.bar(x, y1, tick_label=['FY2013', 'FY2014', 'FY2015', 'FY2016', 'FY2017', 'FY2018', 'FY2019'], width=bar_width)

def autolabel(rects):
    for rect in rects:
        height=rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2,height+300,s='{}'.format(height),ha='center',va='bottom')
autolabel(bar_rects)

plt.title("2013-2019财年淘宝和天猫平台的GMV")
#Fiscal Year
plt.xlabel("财年")
#Gross Merchandise Volume
plt.ylabel("GMV(单位：亿元)")
plt.show()
