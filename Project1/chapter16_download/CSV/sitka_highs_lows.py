#coding=gbk
#美国阿拉斯加州锡特卡2018年每日的最高气温和最低气温

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#设置字体

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期、最高气温、最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#根据最高气温、最低气温绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
#fill_between()接受一个x值和两个y值系列，并填充两个y值之间的空间，alpha表示透明度(0表示完全透明，1表示完全不透明)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图的格式
ax.set_title("2018年每日的最高气温和最低气温",fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)#修改了字体
fig.autofmt_xdate()#绘制倾斜的日期
ax.set_ylabel("温度(F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()