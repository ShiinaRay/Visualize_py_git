import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4, 19)
# x = ['9月4日',]
y_max = np.array([32, 33, 34, 34, 33, 31, 30, 29, 30, 29, 26, 23, 21, 25, 31])
y_min = np.array([19, 19, 20, 22, 22, 21, 22, 16, 18, 18, 17, 14, 15, 16, 16])
# 绘制折线图
plt.plot(x, y_max)
plt.plot(x, y_min)
# 正确显示中文和负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# plt.title('Maximum and minimum temperature in 15 days')
plt.title('北京市未来15天的最高气温和最低气温')
plt.xlabel("日期")
plt.ylabel("气温")
plt.legend(['最高气温', '最低气温'], loc='upper right')
plt.show()
