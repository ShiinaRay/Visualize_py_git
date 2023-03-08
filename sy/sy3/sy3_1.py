import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# x = [x for x in range(1, 13)
x = np.arange(1, 13)
y1 = [20, 28, 23, 16, 29, 36, 39, 33, 31, 19, 21, 25]
y2 = [17, 22, 39, 26, 35, 23, 25, 27, 29, 38, 28, 20]
labels = ['1 月', '2 月', '3 月', '4 月', '5 月', '6 月', '7月', '8 月', '9 月', '10 月', '11 月', '12 月']
ax1 = plt.subplot(211)
# ax1.plot(x, y1, 'm--o', lw=2, ms=5, label='产品A')
# ax1.plot(x, y2, 'g--o', lw=2, ms=5, label='产品B')
ax1.plot(x, y1, lw=2, ms=5, label='产品A', color='skyblue', marker='D', linestyle='--')
ax1.plot(x, y2, lw=2, ms=5, label='产品B', color='pink', marker='o', ls='--')
ax1.set_title("产品A和产品B去年的销售额")
ax1.set_ylim(10, 45)
ax1.set_ylabel('销售额(亿元)')
ax1.set_xlabel('月份')
for xy1 in zip(x, y1):
    ax1.annotate("%s" % xy1[1], xy=xy1, xytext=(-5, 5), textcoords='offset points')
for xy2 in zip(x, y2):
    ax1.annotate("%s" % xy2[1], xy=xy2, xytext=(-5, 5), textcoords='offset points')
ax1.legend()
ax2 = plt.subplot(223)
ax2.pie(y1, radius=1, wedgeprops={'width':0.5}, labels=labels, autopct='%3.1f%%', pctdistance=0.75)
ax2.set_title('产品A的销售额 ')
ax3 = plt.subplot(224)
ax3.pie(y2, radius=1, wedgeprops={'width':0.5}, labels=labels,autopct='%3.1f%%', pctdistance=0.75)
ax3.set_title('产品B的销售额 ')
plt.tight_layout()
plt.show()
