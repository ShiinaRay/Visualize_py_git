import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 16)
y = np.array([5.9, 6.2, 6.7, 7.0, 7.0, 7.1, 7.2, 7.4,
              7.5, 7.6, 7.7, 7.7, 7.7, 7.8, 7.9])
labels = np.array(['宝骏310', '宝马i3', '致享', '焕驰', '力帆530',
                   '派力奥', '悦翔V3', '乐风RV', '奥迪A1', '威驰FS',
                   '夏利N7', '启辰R30', '和悦A13RS', '致炫', '赛欧'])
fig = plt.figure(figsize=(10, 6), dpi= 80)
ax = fig.add_subplot(111)
# 绘制棉棒图
markerline, stemlines, baseline = ax.stem(x, y, linefmt='--',
                                          markerfmt='o', label='TestStem', use_line_collection=True)
# 设置棉棒图线段的属性
plt.setp(stemlines, lw=1)
ax.set_title('不同品牌轿车的燃料消耗量', fontdict={'size':18})
ax.set_ylabel('燃料消耗量(L/km)')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=60)
ax.set_ylim([0, 10])
for temp_x, temp_y in zip(x, y):
    ax.text(temp_x, temp_y + 0.5, s='{}'.format(temp_y), ha='center', va='bottom', fontsize=14)
plt.show()
