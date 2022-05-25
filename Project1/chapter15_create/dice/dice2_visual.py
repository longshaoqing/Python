#coding=gbk
#同时掷2个骰子

from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

#创建两个骰子
sides_1=int(input("请问您第1个骰子想创建多少面？"))
sides_2=int(input("请问您第2个骰子想创建多少面？"))
die_1 = Dice(sides_1)
die_2 = Dice(sides_2)

#同时投掷两个骰子，并将结果保存在results[]
nums=int(input("请问您想将第1个"+str(sides_1)+"面骰子和第2个"+str(sides_2)+"面骰子，同时投掷多少次？"))
results = []
for roll_num in range(nums):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#结果可视化
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]#柱状图

x_axis_config = {'title': '结果', 'dtick': 1}#'dtick': 1，表示刻度间距
y_axis_config = {'title': '结果频率'}
my_layout = Layout(title="第1个"+str(sides_1)+"面骰子和第2个"+str(sides_2)+"面骰子，同时投掷"+str(nums)+"次的结果",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two.html')