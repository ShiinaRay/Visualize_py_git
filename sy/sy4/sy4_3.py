import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

labels = np.array(['武磊登上电影频道', '东京奥运会海报', '浓眉哥', '安东尼准绝杀', '湖人单场20记盖帽',
                   '第77届金球奖红毯', '孟非大赞武磊', '李铁上任', '活塞vs湖人', '英超'])
x = np.arange(1, 11)
num = np.array([62253, 51255, 34541, 28733, 17073, 9000, 5963, 2041, 1879, 1681])
fig = plt.figure(figsize=(10, 6), dpi=80)
ax = fig.add_subplot(111)
markerline, stemlines, baseline = ax.stem(x, num, linefmt='--', markerfmt='o', label='TestStem',
                                          use_line_collection=True)
plt.setp(stemlines, lw=1)
ax.set_title('百度体育热点Top10新闻的搜索指数', fontdict={'size': 18})
ax.set_ylabel('搜索指数')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=60)
for temp_x, temp_y in zip(x, num):ax.text(temp_x, temp_y + 0.5, s='{}'.format(temp_y), ha='center'
                                          , va='bottom', fontsize=14)
plt.show()
