#codeing=utf-8
import bs4      #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error  #指定URL，获取网页数据
import xlwt     #进行Excel操作
import sqlite3  #进行申请利特数据库操作

def main():
    # baseurl="https://maoyan.com/board/4?start="
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist=get(baseurl)
    URL(baseurl)
    # 3.保存数据
    #path = ".\\豆瓣电影Top250.xls"  # Excel格式
    #save(path)

findlink=re.compile(r'<a href="(.*?)">')  #全局变量  正则表达式   (.*?):表示一组内容
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)   #re.s让换行符包含在字符中
findTitle=re.compile(r'<span class="title">(.*)</span>')
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudger=re.compile(r'<span>(\d*)人评价</span>')
#爬取网页
def get(baseurl):
    datalist=[]
    for i in range(0,1):  #调用获取页面信息的函数*10次
        url=baseurl+str(i*25)
        html=URL(url)  #保存获取到的网页源码
        # 2.解析数据（边爬取边解析）
        soup= bs4.BeautifulSoup(html, "html.parser")
        for i in soup.find_all("div",class_="item"):
            # print(i)
            data = []  # 保存一部电影的所有信息
            item = str(i)
            link = re.findall(findlink, item)[0]
            print(link)

    return datalist
def save(path):
    pass

#爬取指定一个url网页内容
def URL(url):
    #模拟浏览器头部信息，向豆瓣服务器发送信息
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52"}
    #向url网址发送请求
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        #请求打开网页
        response=urllib.request.urlopen(request)
        #按utf-8格式读取网页
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if(hasattr(e,"code")):
            print(e.code)
        if(hasattr(e,"reason")):
            print(e.reason)
    return html
if __name__=="__main__":
    main()