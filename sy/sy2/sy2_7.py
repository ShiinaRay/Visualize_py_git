import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

kinds = ['童装', '奶粉', '洗护', '春夏新品', '玩具文娱', '童鞋']
money = [29665 / 63336.2, 3135.4 / 63336.2, 5240.9 / 63336.2, 5633.8 / 63336.2, 9308.1 / 63336.2, 10353 / 63336.2]
# distance = [0.1, 0.1, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1]
# plt.pie(money, labels=kinds, autopct='%3.1f%%', shadow=True, explode=distance, startangle=90)
plt.pie(money, labels=kinds, autopct='%3.1f%%', shadow=True, startangle=90)
plt.title('2019年9月拼多多平台子类销售情况饼图')
plt.legend(['童装', '奶粉', '洗护', '春夏新品', '玩具文娱', '童鞋'], loc=(1, 0.7))
plt.table(cellText=[[29665, 3135.4, 5240.9, 5633.8, 9308.1, 10353]], colWidths=[0.1] * 6, rowLabels=['销售额（单位：亿元）'],
          colLabels=['童装', '奶粉', '洗护', '春夏新品', '玩具文娱', '童鞋'], loc='bottom')
plt.show()
