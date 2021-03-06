#coding=gbk

#美国纽约2022年1月1日至2022年5月21日的每日最高气温和最低气温可视化图

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#设置字体

filename = 'data/NewYork.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期、最高气温、最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[6])
        low = int(row[7])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#根据最高气温和最低气温绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#最高气温和最低气温之间用蓝色填充
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#绘图格式
title = "2022年1月1日至2022年5月21日的每日最高气温和最低气温\n美国纽约"
ax.set_title(title,fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)
fig.autofmt_xdate()#绘制倾斜的日期
ax.set_ylabel("温度(F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()