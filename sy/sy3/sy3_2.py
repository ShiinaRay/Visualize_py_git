import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def autolabel(ax, rects):
    for rect in rects:
        width = rect.get_width()
        ax.text(width  + 3, rect.get_y() , s='{}'.format(width), ha='center', va='bottom')
y = np.arange(12)
x1 = np.array([19, 33, 28, 29, 14, 24, 57, 6, 26, 15, 27, 39])
x2 = np.array([25, 33, 58, 39, 15, 64, 29, 23, 22, 11, 27, 50])
labels = np.array(['中国', '加拿大', '巴西', '澳大利亚', '日本', '墨西哥',
                   '俄罗斯', '韩国', '瑞士', '土耳其', '英国', '美国'])
fig, (ax1, ax2) = plt.subplots(1, 2)
# barh1_rects = ax1.barh(y, x1, height=0.5, tick_label=labels, color='#FFA500')
barh1_rects = ax1.barh(y, x1, height=0.5, tick_label=labels, color='skyblue')
ax1.set_xlabel('人群比例(%)')
ax1.set_title('部分国家养猫人群的比例52')
ax1.set_xlim(0, x1.max() + 10)
autolabel(ax1, barh1_rects)
# barh2_rects = ax2.barh(y, x2, height=0.5, tick_label=labels, color='#20B2AA')
barh2_rects = ax2.barh(y, x2, height=0.5, tick_label=labels, color='pink')
ax2.set_xlabel('人群比例(%)')
ax2.set_title('部分国家养狗人群的比例52')
ax2.set_xlim(0, x2.max() + 10)
autolabel(ax2, barh2_rects)
plt.tight_layout()
plt.show()
