#coding=gbk


from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

#��������
sides=int(input("�������봴��һ������������ӣ�"))
die = Dice(sides)
#Ͷ���������Ӳ��������¼��results[]�б�
nums=int(input("�������뽫"+str(sides)+"������Ͷ�����ٴΣ�"))
results = []
for roll_num in range(nums):
    result = die.roll()
    results.append(result)
    
#�������
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)#�����ӵ�������
    frequencies.append(frequency)#��ÿ������ֵ��ܴ�����¼��frequencies[]
    
#������ӻ�
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]#��״ͼ

x_axis_config = {'title': '���'}
y_axis_config = {'title': '���Ƶ��'}
my_layout = Layout(title="Ͷ��"+str(sides)+"������"+str(nums)+"�εĽ��",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='one.html')
