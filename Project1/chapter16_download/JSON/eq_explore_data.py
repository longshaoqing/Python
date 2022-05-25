#coding=gbk

import json
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #json.load()将数据转换为Python能够处理的格式
all_eq_dicts = all_eq_data['features']#提取与键features相关联的数据
mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']#将震级存储在properties 的 mag 键下
    title = eq_dict['properties']['title']#位置列表
    lon = eq_dict['geometry']['coordinates'][0]#经度
    lat = eq_dict['geometry']['coordinates'][1]#纬度
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)


if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])
