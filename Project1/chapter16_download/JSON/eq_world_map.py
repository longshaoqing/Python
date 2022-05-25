#coding=gbk
#全球地震散点图：JSON格式

import json
import plotly.express as px
import pandas as pd

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级'])

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200], #经度的范围
    range_y=[-90, 90], #纬度的范围
    width=800,  #设置宽度像素
    height=800, #设置高度像素
    title='全球地震散点图',
    size='震级',  #使用size参数指定散点图中每个标记的尺寸
    size_max=10, #标记尺寸设置为10像素
    color='震级', #根据震级严重程度设置散点的颜色
    hover_name='位置', #鼠标指向时显示文本
)
#fig.write_html()可将可视化图保存为html文件
fig.write_html('global_earthquakes.html')
fig.show()

if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])

