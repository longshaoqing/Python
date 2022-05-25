#coding=gbk
#使用Plotly可视化仓库，绘GitHub最受欢迎的Java项目图

import requests
from plotly.graph_objs import Bar
from plotly import offline

#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:Java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #状态码200表示请求成功

#处理结果
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name'] #项目名
    repo_url = repo_dict['html_url'] #项目URL
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" #项目连接

    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']    #项目所有者
    description = repo_dict['description'] #项目描述
    label = f"{owner}<br />{description}"
    labels.append(label)

#可视化
data = [{
    'type': 'bar', #柱状图
    'x': repo_links, #x轴设置为可点击链接
    'y': stars,
    'hovertext': labels, #自定义工具提示
    'marker': {   #maker设置影响条形设计
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6, #不透明度为0.6
}]

my_layout = {
    'title': 'GitHub最受欢迎的Java项目',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': '仓库',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': '星数',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Java_repos.html')
