#coding=gbk

import requests
#ִ��API���ò��洢��Ӧ
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") #״̬��200��ʾ����ɹ�

#��API��Ӧ��ֵ��һ������
response_dict = r.json()
#��ӡ��'total_count'�������ֵ����ָ��GitHub�ܹ��ж��ٸ�Python�ֿ�
print(f"Total repositories: {response_dict['total_count']}")

#̽���йزֿ����Ϣ��'items'��ֵ��һ���ֵ��б�ÿ���ֵ����һ��Python�ֿ����Ϣ
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")#��ȡ�˶��ٸ��ֿ���Ϣ

print("\nÿ���ѻ�ȡ�ֿ����Ϣ:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}") #��Ŀ��
    print(f"Owner: {repo_dict['owner']['login']}") #���������ߵ��ֵ�
    print(f"Stars: {repo_dict['stargazers_count']}") #��Ŀ�ȼ�
    print(f"Repository: {repo_dict['html_url']}") #��Ŀ��URL
    print(f"Created: {repo_dict['created_at']}") #��Ŀ�Ĵ���ʱ��
    print(f"Updated: {repo_dict['updated_at']}\n") #��Ŀ���һ�θ��µ�ʱ��