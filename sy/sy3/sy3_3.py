import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
month_x = np.arange(1, 13, 1)
data_tem = np.array([2.0, 2.2, 3.3, 4.5, 6.3, 10.2,
                     20.3, 33.4, 23.0, 16.5, 12.0, 6.2])
data_precipitation = np.array([2.6, 5.9, 9.0, 26.4, 28.7, 70.7,
                               175.6, 182.2, 48.7, 18.8, 6.0, 2.3])
data_evaporation = np.array([2.0, 4.9, 7.0, 23.2, 25.6, 76.7,
                             135.6, 162.2, 32.6, 20.0, 6.4, 3.3])
fig, ax = plt.subplots()
bar_ev = ax.bar(month_x, data_evaporation, color='skyblue', tick_label=['1月', '2月', '3月', '4月', '5月', '6月',
                                                                        '7月', '8月', '9月', '10月', '11月', '12月'])
bar_pre = ax.bar(month_x, data_precipitation, bottom=data_evaporation, color='pink')
ax.set_ylabel('水量 (ml)')
ax.set_title('某地区全年的平均气温与降水量、蒸发量')
ax_right = ax.twinx()
line = ax_right.plot(month_x, data_tem, 'D--r')
# ax_right.set_ylabel('气温($^\circ$C)')
ax_right.set_ylabel('平均气温(℃)')
plt.legend([bar_ev, bar_pre, line[0]], ['蒸发量', '降水量', '平均气温'],
           shadow=True, fancybox=True)
plt.show()
