# BeautifulSoup4 将复杂的HTML文档抓成一个复杂的树形结构，每个节点都是Python对象，所有对象都可以归纳为3种：
# 1.Tag             标签及其内容：默认拿第一个
# NavigableString   标签里的内容（字符串）
# BeautifulSoup     表示整个文档

from bs4 import BeautifulSoup
file=open("./baidu.html","rb")#用二进制方式打开文件
html=file.read().decode("utf-8")#读文件
bs=BeautifulSoup(html,"html.parser")#解析html解析器，解析html文档，形成树形结构
print(bs.title)#获取标签及其内容
print(bs.title.string)#只获取内容
print(bs.a.attrs) #字典方式获取属性

print("--------------------------------------")
#文档遍历
print(bs.head.contents[1])

#文档搜素

#(1)find_all()
#list=bs.find_all("a")
import re
#正则表达式搜索：使用re.compile()方法来匹配内容
#list=bs.find_all(re.compile("a"))
# for i in list:
#     print(i)
#(2)参数
#list=bs.find_all(id="div1")
# list=bs.find_all(class_="Title")
# for i in list:
#     print(i)
#(3)文本
# list=bs.find_all(text="hao123")
# for i in list:
#     print(i)
# list=bs.find_all(text=re.compile("\d"))#应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for i in list:
#     print(i)
#(4)limit  参数
# list=bs.find_all("a",limit=3)
# for i in list:
#     print(i)

# css选择器
#list=bs.select("title")#通过标签查找
# list=bs.select("#div1")#通过id查找
# list=bs.select(".Title")#通过class查找
# list=bs.select("a[class='bai']")#通过属性查找
list=bs.select("head > title")#通过子标签查找
for i in list:
    print(i)
