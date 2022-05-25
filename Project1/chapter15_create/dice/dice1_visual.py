#coding=gbk


from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

#创建骰子
sides=int(input("请问您想创建一个多少面的骰子？"))
die = Dice(sides)
#投掷几次骰子并将结果记录到results[]列表
nums=int(input("请问您想将"+str(sides)+"面骰子投掷多少次？"))
results = []
for roll_num in range(nums):
    result = die.roll()
    results.append(result)
    
#分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)#对骰子点数计数
    frequencies.append(frequency)#将每个点出现的总次数记录到frequencies[]
    
#结果可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]#柱状图

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果频率'}
my_layout = Layout(title="投掷"+str(sides)+"面骰子"+str(nums)+"次的结果",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='one.html')
