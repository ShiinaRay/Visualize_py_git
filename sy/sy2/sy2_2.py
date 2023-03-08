import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

kinds = ['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它']
money = [800 / 3000, 100 / 3000, 1000 / 3000, 200 / 3000, 300 / 3000, 200 / 3000, 200 / 3000, 200 / 3000]
distance = [0.1, 0.1, 0.15, 0.1, 0.1, 0.1, 0.1, 0.1]
plt.pie(money, labels=kinds, autopct='%3.1f%%', shadow=True, explode=distance, startangle=90)
plt.title('用户A某月使用支付宝的消费明细')
# plt.legend(['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它'], loc='lower left')
# plt.legend(['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它'], loc = (1.05, 0.7))
# plt.legend(['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它'], loc=(-0.3, -0.13)
#            , title='图例')
plt.legend(['购物', '人情往来', '餐饮美食', '通信物流', '生活日用', '交通出行', '休闲娱乐', '其它'], loc=(-0.3, -0.1))
plt.show()
