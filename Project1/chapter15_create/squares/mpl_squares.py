#coding=gbk

"""����ƽ����������ͼ"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')#������ʽ
fig, ax = plt.subplots()#������ͼ��fig��ʾ����ͼƬ��as��ʾͼƬ�еĸ���ͼ��
ax.plot(input_values, squares, linewidth=3)#��������ֵinput_values�����ֵsquares��������ͼ

#���ñ�ǩ
ax.set_title("ƽ����",fontproperties=my_font)#����
ax.set_xlabel("ֵ",fontproperties=my_font)#x��
ax.set_ylabel("ֵ��ƽ��",fontproperties=my_font)#y��

#���ÿ̶ȱ�Ǵ�С
ax.tick_params(axis='both', labelsize=14)

plt.show()#��ʾͼ��
