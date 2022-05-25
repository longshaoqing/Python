#coding=gbk
#��������˹�������ؿ�2018��ÿ�յ�������º��������

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #���ļ��л�ȡ���ڡ�������¡��������
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#����������¡�������»�ͼ
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#fill_between()����һ��xֵ������yֵϵ�У����������yֵ֮��Ŀռ䣬alpha��ʾ͸����(0��ʾ��ȫ͸����1��ʾ��ȫ��͸��)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#����ͼ�ĸ�ʽ
ax.set_title("2018��ÿ�յ�������º��������",fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)#�޸�������
fig.autofmt_xdate()#������б������
ax.set_ylabel("�¶�(F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()