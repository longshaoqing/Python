#coding=gbk

"""����ƽ������ɢ��ͼ"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

x_values = range(1, 1001)#x�᣺1~1000
y_values = [x**2 for x in x_values]#y�᣺1^2~1000^2

plt.style.use('seaborn')#������ʽ
fig, ax = plt.subplots()#������ͼ��fig��ʾ����ͼƬ��as��ʾͼƬ�еĸ���ͼ��
#����c���ó�yֵ�б���ʹ��cmap����pyplotʹ��˵����ɫӳ�䣬s��ʾɢ��ĳߴ�
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#���ñ�ǩ
ax.set_title("ƽ����",fontproperties=my_font)
ax.set_xlabel("ֵ",fontproperties=my_font)
ax.set_ylabel("ֵ��ƽ��",fontproperties=my_font)

#���ÿ̶ȱ�Ǵ�С
ax.tick_params(axis='both', which='major', labelsize=14)

#��������ȡַ��Χ��x����[0,1100],y����[0,1100000]
ax.axis([0, 1100, 0, 1100000])

plt.show()#��ʾͼ��
plt.savefig("squares.png")