import urllib.request
#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8")) #decode用utf-8的格式解码

#获取post请求(浏览器请求)
import urllib.parse #解析字典（键值对）
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))

#获取get请求
#超时处理
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode("utf-8"))
# except:
#     print("time out!")

# response=urllib.request.urlopen("http://douban.com")
# print(response.read().decode("utf-8")) #HTTP Error 418:发现你是爬虫了

#post方式
#url="http://douban.com"
#url="http://httpbin.org/post"
#headers是字典
# headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"}
# data=bytes(urllib.parse.urlencode({"name":"long"}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="post")
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#get方式
url="http://douban.com"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"}
req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))