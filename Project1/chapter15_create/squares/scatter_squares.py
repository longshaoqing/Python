#coding=gbk

"""绘制平方序列散点图"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#设置字体

x_values = range(1, 1001)#x轴：1~1000
y_values = [x**2 for x in x_values]#y轴：1^2~1000^2

plt.style.use('seaborn')#设置样式
fig, ax = plt.subplots()#创建子图，fig表示整张图片，as表示图片中的各个图表
#参数c设置成y值列表，并使用cmap告诉pyplot使用说明颜色映射，s表示散点的尺寸
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#设置标签
ax.set_title("平方数",fontproperties=my_font)
ax.set_xlabel("值",fontproperties=my_font)
ax.set_ylabel("值的平方",fontproperties=my_font)

#设置刻度标记大小
ax.tick_params(axis='both', which='major', labelsize=14)

#设置坐标取址范围：x属于[0,1100],y属于[0,1100000]
ax.axis([0, 1100, 0, 1100000])

plt.show()#显示图表
plt.savefig("squares.png")