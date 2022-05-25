# coding=gbk
#同时投掷2个骰子

from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

# 创建两个骰子
sides_1 = int(input("请问您第1个骰子想创建多少面？"))
sides_2 = int(input("请问您第2个骰子想创建多少面？"))
sides_3 = int(input("请问您第3个骰子想创建多少面？"))
dice_1 = Dice(sides_1)
dice_2 = Dice(sides_2)
dice_3 = Dice(sides_3)

# 同时投掷3个骰子，并将结果保存在results[]
nums = int(input("请问您想将第1个" + str(sides_1) + "面骰子、第2个" + str(sides_2) + "面骰子、第3个"+
                 str(sides_3) + "面骰子，同时投掷多少次？"))
results = []
for roll_num in range(nums):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]  # 柱状图

x_axis_config = {'title': '结果', 'dtick': 1}  # 'dtick': 1，表示刻度间距
y_axis_config = {'title': '结果频率'}
my_layout = Layout(title="第1个" + str(sides_1) + "面骰子、第2个" + str(sides_2) + "面骰子、第3个"+str(sides_3)
                         +"面骰子，同时投掷" + str(nums) + "次的结果",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='three.html')