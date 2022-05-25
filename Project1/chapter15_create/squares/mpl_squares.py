#coding=gbk

"""绘制平方序列折线图"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#设置字体

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')#设置样式
fig, ax = plt.subplots()#创建子图，fig表示整张图片，as表示图片中的各个图表
ax.plot(input_values, squares, linewidth=3)#根据输入值input_values和输出值squares绘制折线图

#设置标签
ax.set_title("平方数",fontproperties=my_font)#标题
ax.set_xlabel("值",fontproperties=my_font)#x轴
ax.set_ylabel("值的平方",fontproperties=my_font)#y轴

#设置刻度标记大小
ax.tick_params(axis='both', labelsize=14)

plt.show()#显示图表
