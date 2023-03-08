import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

y = np.arange(15)
x = np.array([48.57, 46.18, 42.05, 21.83, 17.03, 16.70, 14.01, 13.84, 12.85, 11.38, 10.25, 9.46, 9.27, 8.88, 8.64])
bar_height = 0.5
plt.barh(y, x, tick_label=['哪吒之魔童降世', '流浪地球', '复仇者联盟4：终局之战', '疯狂的外星人', '飞驰人生', '烈火英雄'
    , '蜘蛛侠：英雄远征', '速度与激情：特别行动', '扫毒2：天地对决', '大黄蜂', '惊奇队长', '比悲伤更悲伤的故事', '哥斯拉2：怪兽之王'
    , '阿丽塔：战斗天使', '银河补习班'], height=bar_height)
plt.title('2019年中国电影票房排行榜Top15')
plt.ylabel("电影名称")
plt.xlabel("总票房（亿元）")
plt.show()
