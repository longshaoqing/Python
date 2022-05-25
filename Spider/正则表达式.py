#正则表达式
import re

pat=re.compile("AA") #用re创建对象，compile声明标准(正则表达式)
m=pat.search("CBAAC")  #search是被校验的内容
print(m)
print("-------------")
n=re.search("asc","asfkuladjasc")#一行解决，前面是标准(正则表达式)，后面是校验内容
print(n)
print("-------------")
k=re.findall("[A-Z]+","asfSkuOadFQIasc")
print(k)
print("-------------")
a=re.sub("a","A","asfSkuOadFQIasc") # 替换：a被A替换
print(a)
b=r"\sdfl-\'"  #正则表达式，前面加上r，表示直接输出（不用担心转移字符问题）
print(b)