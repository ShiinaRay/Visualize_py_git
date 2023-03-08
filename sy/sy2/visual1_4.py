import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

y = np.arange(18)
x = np.array([0.959, 0.951, 0.935, 0.924, 0.893, 0.892, 0.865, 0.863, 0.86, 0.856, 0.854, 0.835, 0.826, 0.816
                 , 0.798, 0.765, 0.763, 0.67])
bar_height = 0.5
plt.barh(y, x, tick_label=['家政，家教，保姆服务', '飞机票火车票', '家具', '手机及其配件', '计算机及其配件', '汽车用品'
    , '游戏充值', '个人护理用品', '书报杂志音像制品', '餐饮，旅游，住宿', '家用电器', '食品饮料烟酒保健品', '家庭日杂用品'
    , '保险演出票务', '服装鞋帽家用纺织品', '数码产品', '其它商品和服务', '工艺品收藏品'], height=bar_height)
plt.title('各商品种类的网购替代率')
plt.ylabel("商品种类")
plt.xlabel("网购替代率")
plt.show()
