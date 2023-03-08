import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

kinds = ['面粉', '全麦粉', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖']
money = [250 / 758, 150 / 758, 4 / 758, 250 / 758, 50 / 758, 30 / 758, 4 / 758, 20 / 758]
# distance = [0.1, 0.1, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1]
# plt.pie(money, labels=kinds, autopct='%3.1f%%', shadow=True, explode=distance, startangle=90)
plt.pie(money, labels=kinds, autopct='%3.1f%%', shadow=True, startangle=90)
plt.title('果酱面包配料饼图')
# plt.legend(['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它'], loc=(-0.3, -0.1))
plt.legend(['面粉', '全麦粉', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖'], loc=(1, 0.7))
plt.table(cellText=[[250, 150, 4, 250, 50, 30, 4, 20]], colWidths=[0.1] * 8, rowLabels=['重量（g）'],
          colLabels=['面粉', '全麦粉', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖'], loc='bottom')
# plt.table(cellText=[[250, 150, 4, 250, 50, 30, 4, 20]], colWidths=[0.1] * 8, rowLabels=['重量（g）'],
#           colLabels=['面粉', '全麦粉', '酵母', '苹果酱', '鸡蛋', '黄油', '盐', '白糖'], loc='lower right')
plt.show()
