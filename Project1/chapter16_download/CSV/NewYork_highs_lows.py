#coding=gbk

#����ŦԼ2022��1��1����2022��5��21�յ�ÿ��������º�������¿��ӻ�ͼ

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

filename = 'data/NewYork.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #���ļ��л�ȡ���ڡ�������¡��������
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[6])
        low = int(row[7])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#����������º�������»�ͼ
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#������º��������֮������ɫ���
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#��ͼ��ʽ
title = "2022��1��1����2022��5��21�յ�ÿ��������º��������\n����ŦԼ"
ax.set_title(title,fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)
fig.autofmt_xdate()#������б������
ax.set_ylabel("�¶�(F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()