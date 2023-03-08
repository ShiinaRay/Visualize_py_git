import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([2590, 1450, 877, 1984, 2109])
y = np.array([0.2, 0.19, 0.08, 0.09, 0.22])
area = np.array([(0.19 * 150) ** 2, (0.14 * 150) ** 2, (0.05 * 150) ** 2, (0.15 * 150) ** 2, (0.17 * 150) ** 2])
plt.scatter(x, y, s=area)
plt.title('各产品销售情况')
plt.xlabel("销售金额（万元）")
plt.ylabel("利润率")
plt.show()
