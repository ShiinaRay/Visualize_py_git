import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x1 = np.array([5200, 5254.5, 5283.4, 5107.8, 5443.3, 5550.6, 6400.2, 6404.9, 5483.1, 5330.2, 5543, 6199.9])
x2 = np.array([4605.2, 4710.3, 5168.9, 4767.2, 4947, 5203, 6047.4, 5945.5, 5219.6, 5038.1, 5196.3, 5698.6])

plt.boxplot([x1, x2], vert=False, meanline=True, widths=0.4,
            patch_artist=True,
            showmeans=True,
            labels=['2018年', '2017年'])
plt.title('2017年和2018年全国发电量统计')
plt.ylabel("年份")
plt.xlabel("发电量（亿千万·时）")
plt.show()
