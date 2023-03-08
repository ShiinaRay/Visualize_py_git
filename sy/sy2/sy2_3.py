import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
y = np.array([0.5, 2.0, 4.4, 7.9, 12.3, 17.7, 24.1, 31.5, 39.9, 49.2, 59.5, 70.8, 83.1, 96.4, 110.7, 126.0, 142.2
                 , 159.4, 177.6, 196.8])

plt.scatter(x,y)
plt.title('车速与制动距离的关系')
plt.xlabel("车速(km/h)")
plt.ylabel("制动距离(m)")
plt.xlim(10, 200)
plt.grid()
# plt.axhline()
plt.show()
