#coding=gbk

import requests
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #状态码200表示请求成功

#将API响应赋值给一个变量
response_dict = r.json()
#打印与'total_count'相关联的值，它指出GitHub总共有多少个Python仓库
print(f"Total repositories: {response_dict['total_count']}")

#探索有关仓库的信息，'items'的值是一个字典列表，每个字典包含一个Python仓库的信息
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")#获取了多少个仓库信息

print("\n每个已获取仓库的信息:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}") #项目名
    print(f"Owner: {repo_dict['owner']['login']}") #访问所有者的字典
    print(f"Stars: {repo_dict['stargazers_count']}") #项目等级
    print(f"Repository: {repo_dict['html_url']}") #项目的URL
    print(f"Created: {repo_dict['created_at']}") #项目的创建时间
    print(f"Updated: {repo_dict['updated_at']}\n") #项目最后一次更新的时间