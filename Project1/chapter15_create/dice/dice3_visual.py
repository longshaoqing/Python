# coding=gbk
#ͬʱͶ��2������

from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

# ������������
sides_1 = int(input("��������1�������봴�������棿"))
sides_2 = int(input("��������2�������봴�������棿"))
sides_3 = int(input("��������3�������봴�������棿"))
dice_1 = Dice(sides_1)
dice_2 = Dice(sides_2)
dice_3 = Dice(sides_3)

# ͬʱͶ��3�����ӣ��������������results[]
nums = int(input("�������뽫��1��" + str(sides_1) + "�����ӡ���2��" + str(sides_2) + "�����ӡ���3��"+
                 str(sides_3) + "�����ӣ�ͬʱͶ�����ٴΣ�"))
results = []
for roll_num in range(nums):
    result = dice_1.roll() + dice_2.roll() + dice_3.roll()
    results.append(result)

# �������
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# ������ӻ�
x_values = list(range(3, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]  # ��״ͼ

x_axis_config = {'title': '���', 'dtick': 1}  # 'dtick': 1����ʾ�̶ȼ��
y_axis_config = {'title': '���Ƶ��'}
my_layout = Layout(title="��1��" + str(sides_1) + "�����ӡ���2��" + str(sides_2) + "�����ӡ���3��"+str(sides_3)
                         +"�����ӣ�ͬʱͶ��" + str(nums) + "�εĽ��",xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='three.html')