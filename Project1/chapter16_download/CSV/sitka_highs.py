#coding=gbk
#��������˹�������ؿ�2018��7��ÿ������¶�

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #���������
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#��������

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #���ļ��л�ȡ���ں�����¶�,
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

#��������¶Ȼ�ͼ
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#����ͼ�ĸ�ʽ
ax.set_title("2018��7��ÿ������¶�", fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)#�޸�������
fig.autofmt_xdate()#������б������
ax.set_ylabel("�¶� (F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()