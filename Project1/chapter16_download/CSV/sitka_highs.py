#coding=gbk
#美国阿拉斯加州锡特卡2018年7月每日最高温度

import csv
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties #字体管理器
my_font = FontProperties(fname=r'C:\WINDOWS\FONTS\SIMSUN.TTC',size=20)#设置字体

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期和最高温度,
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

#根据最高温度绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

#设置图的格式
ax.set_title("2018年7月每日最高温度", fontproperties=my_font)
ax.set_xlabel('',fontproperties=my_font)#修改了字体
fig.autofmt_xdate()#绘制倾斜的日期
ax.set_ylabel("温度 (F)",fontproperties=my_font)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()