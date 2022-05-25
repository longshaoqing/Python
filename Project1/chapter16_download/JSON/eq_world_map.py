#coding=gbk
#ȫ�����ɢ��ͼ��JSON��ʽ

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

data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['����', 'γ��', 'λ��', '��'])

fig = px.scatter(
    data,
    x='����',
    y='γ��',
    range_x=[-200, 200], #���ȵķ�Χ
    range_y=[-90, 90], #γ�ȵķ�Χ
    width=800,  #���ÿ������
    height=800, #���ø߶�����
    title='ȫ�����ɢ��ͼ',
    size='��',  #ʹ��size����ָ��ɢ��ͼ��ÿ����ǵĳߴ�
    size_max=10, #��ǳߴ�����Ϊ10����
    color='��', #���������س̶�����ɢ�����ɫ
    hover_name='λ��', #���ָ��ʱ��ʾ�ı�
)
#fig.write_html()�ɽ����ӻ�ͼ����Ϊhtml�ļ�
fig.write_html('global_earthquakes.html')
fig.show()

if __name__ == '__main__':
    print(mags[:5])
    print(titles[:5])
    print(lons[:5])
    print(lats[:5])

