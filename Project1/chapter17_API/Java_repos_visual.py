#coding=gbk
#ʹ��Plotly���ӻ��ֿ⣬��GitHub���ܻ�ӭ��Java��Ŀͼ

import requests
from plotly.graph_objs import Bar
from plotly import offline

#ִ��API���ò��洢��Ӧ
url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #״̬��200��ʾ����ɹ�

#������
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name'] #��Ŀ��
    repo_url = repo_dict['html_url'] #��ĿURL
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" #��Ŀ����

    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']    #��Ŀ������
    description = repo_dict['description'] #��Ŀ����
    label = f"{owner}<br />{description}"
    labels.append(label)

#���ӻ�
data = [{
    'type': 'bar', #��״ͼ
    'x': repo_links, #x������Ϊ�ɵ������
    'y': stars,
    'hovertext': labels, #�Զ��幤����ʾ
    'marker': {   #maker����Ӱ���������
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6, #��͸����Ϊ0.6
}]

my_layout = {
    'title': 'GitHub���ܻ�ӭ��Java��Ŀ',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '�ֿ�',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '����',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Java_repos.html')
