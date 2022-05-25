#coding=gbk
#�������ݸ�����������2018��ÿ��������º�������»�ͼ

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #���ļ��л�ȡ���ڡ�������¡��������
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"{current_date}�����ݶ�ʧ��")
        else:
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
title = "2018��ÿ��������º��������\n�������ݸ�����������"
ax.set_title(title,fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)
fig.autofmt_xdate()#������б������
ax.set_ylabel("�¶�(F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()