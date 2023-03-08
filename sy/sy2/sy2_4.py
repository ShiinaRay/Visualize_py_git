import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = np.arange(6)
y_man = np.array([90.5, 89.5, 88.7, 88.5, 85.2, 86.6])
y_woman = np.array([92.7, 87.0, 90.5, 85.0, 89.5, 89.8])
bar_width = 0.25
plt.bar(x, y_man, tick_label=['高二1班', '高二2班', '高二3班', '高二4班', '高二5班', '高二6班']
        , width=bar_width)
plt.bar(x + bar_width + 0.1, y_woman, width=bar_width)
plt.title('高二各班男生、女生英语平均成绩')
plt.xlabel("班级名称")
plt.ylabel("平均成绩")
plt.axhline(88.625, linestyle='--')
# plt.axhline(88.625, ls='--')
# plt.axhline(88.625, ls='-')
# plt.axhline(88.625)
plt.legend(['全体平均成绩', '男生平均成绩', '女生平均成绩'], loc='lower right')
plt.show()
