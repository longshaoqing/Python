#coding=gbk
#ͬʱ��2������

from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

#������������
sides_1=int(input("��������1�������봴�������棿"))
sides_2=int(input("��������2�������봴�������棿"))
die_1 = Dice(sides_1)
die_2 = Dice(sides_2)

#ͬʱͶ���������ӣ��������������results[]
nums=int(input("�������뽫��1��"+str(sides_1)+"�����Ӻ͵�2��"+str(sides_2)+"�����ӣ�ͬʱͶ�����ٴΣ�"))
results = []
for roll_num in range(nums):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
#�������
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#������ӻ�
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]#��״ͼ

x_axis_config = {'title': '���', 'dtick': 1}#'dtick': 1����ʾ�̶ȼ��
y_axis_config = {'title': '���Ƶ��'}
my_layout = Layout(title="��1��"+str(sides_1)+"�����Ӻ͵�2��"+str(sides_2)+"�����ӣ�ͬʱͶ��"+str(nums)+"�εĽ��",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='two.html')