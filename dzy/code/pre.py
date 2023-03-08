# 读取数据
import pandas as pd

data5 = pd.read_csv('../data/订单表2018-5.csv', encoding='gbk')
data6 = pd.read_csv('../data/订单表2018-6.csv', encoding='gbk')
data7 = pd.read_csv('../data/订单表2018-7.csv', encoding='gbk')
data8 = pd.read_csv('../data/订单表2018-8.csv', encoding='gbk')
data9 = pd.read_csv('../data/订单表2018-9.csv', encoding='gbk')
print(data5.shape, data6.shape, data7.shape, data8.shape, data9.shape)

# 合并订单表
data = pd.concat([data5, data6, data7, data8, data9], ignore_index=True)

# 删除订单表中的缺失值
data = data.dropna(how='any')

# 增加“市”字段
data['市'] = data['省市区'].str[3: 6]

# 处理订单表中的“商品详情”字段，删除无用字符
del_str = [' ', '(', ')', '（', '）', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'g', 'l', 'm', 'M', 'L',
           '听', '特', '饮', '罐', '瓶', '只', '装', '欧', '式', '&', '%', 'X', 'x', ';']
for i in del_str:
    data['商品详情'] = data['商品详情'].str.replace(i, '')
data['商品名称'] = data['商品详情']

# 删除“总金额（元）”字段中订单金额很小的记录
data = data[data['总金额(元)'] >= 0.5]

# 降维订单数据，删除部分字段
data = data.drop(['手续费(元)', '收款方', '退款金额(元)', '商品详情', '省市区', '软件版本'], axis=1)

# 将时间规约转换为特定的时间格式
data['下单时间'] = pd.to_datetime(data['下单时间'])
data['小时'] = data['下单时间'].dt.hour
data['月份'] = data['下单时间'].dt.month
data['下单时间段'] = 'time'
expression1 = data['小时'] <= 5  # 用于判断条件为凌晨的表达式
data.loc[expression1, '下单时间段'] = '凌晨'  # 条件为真则下单时间段为凌晨
expression2 = (5 < data['小时']) & (data['小时'] <= 8)
data.loc[expression2, '下单时间段'] = '早晨'
expression3 = (8 < data['小时']) & (data['小时'] <= 11)
data.loc[expression3, '下单时间段'] = '上午'
expression4 = (11 < data['小时']) & (data['小时'] <= 13)
data.loc[expression4, '下单时间段'] = '中午'
expression5 = (13 < data['小时']) & (data['小时'] <= 16)
data.loc[expression5, '下单时间段'] = '下午'
expression6 = (16 < data['小时']) & (data['小时'] <= 19)
data.loc[expression6, '下单时间段'] = '傍晚'
expression7 = (19 < data['小时']) & (data['小时'] <= 24)
data.loc[expression7, '下单时间段'] = '晚上'

# 导出保存预处理过的数据用于可视化
data.to_csv('../pre_data/pre_order.csv', index=False, encoding='gbk')
