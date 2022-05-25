import pymysql

def connect(sql):
    # 1.连接
    con = pymysql.connect(host="localhost", user="root", password="123", database="test1")  # database：数据库名
    try:
        #2.创建光标
        cursor=con.cursor()
        #3。执行sql
        cursor.execute(sql)
        #4.封装结果集
        result=cursor.fetchall()
        #5.提交（增删改都要）
        con.commit()
        return result
    except:
        print("数据库连接失败！")
    finally:
        #关闭连接
        con.close()

def connect1(sql,values):
    # 1.连接
    con = pymysql.connect(host="localhost", user="root", password="123", database="test1")  # database：数据库名
    try:
        #2.创建光标
        cursor=con.cursor()
        #3。执行sql
        cursor.execute(sql,values)
        #4.封装结果集
        result=cursor.fetchall()
        #5.提交（增删改都要）
        con.commit()
        return result
    except:
        print("数据库连接失败！")
    finally:
        #关闭连接
        con.close()

def search():
    try:
        db=pymysql.connect(host="localhost",user="root",password="123",database="test1") #database：数据库名
        cursor=db.cursor()
        sql="select * from emp" #emp：表名
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            print(i)
        print("数据库连接成功！")
    except:
        print("数据库连接失败！")
def search1():
    #select 属性 from 表名
    sql = "select * from emp"  # emp：表名
    values=()
    try:
        # 遍历输出结果集
        for i in connect1(sql,values):
            print(i)
        print("查询成功！")
        menu()
    except:
        print("查询失败！")
def add():
    #insert into 表名(属性1，属性2,...) values (值1,值2,...)
    sql="insert into emp(id,name,old) values (%s,%s,%s)"
    id=int(input("请输入id："))
    name=input("请输入name：")
    old=int(input("请输入old："))
    values=(id,name,old)
    try:
        connect1(sql,values)
        print("新增成功！")
        menu()
    except:
        print("新增失败！")
def modify():
    #update 表名 set 属性
    id=int(input("请输入要修改的id："))
    print("1.修改name     2.修改old")
    answer=int(input("请输入1或者2:"))
    if(answer==1):
        sql = "update emp set name=%s where id=%s"
        name=input("name修改为：")
        values=(name,id)
        try:
            connect1(sql, values)
            print("修改name成功！")
            menu()
        except:
            print("修改name失败！")
    elif(answer==2):
        sql = "update emp set old=%s where id=%s"
        old=input("old修改为：")
        values=(old,id)
        try:
            connect1(sql, values)
            print("修改old成功！")
            menu()
        except:
            print("修改old失败！")
    else:
        print("请重新操作！")
        modify()

def delete():
    #delete from 表名
    id=int(input("请输入要删除的id："))
    sql="delete from emp where id=%s "
    values=(id)
    try:
        connect1(sql, values)
        print("删除成功！")
        menu()
    except:
        print("删除失败！")
def delete_table():#删除表
    sql="drop table if exists girl"
    try:
        connect(sql)
        print("删除表成功！")
    except:
        print("删除表失败！")
def quit():
    print("欢迎使用！")

def menu():
    print("=========数据库操作===========")
    print("*****************************")
    print("|         1.新增             |")
    print("|         2.修改             |")
    print("|         3.删除             |")
    print("|         4.查询             |")
    print("|         5.退出             |")
    print("*****************************")
    answer=int(input("请输入编号："))
    if(answer==1):
        add()
    elif(answer==2):
        modify()
    elif(answer==3):
        delete()
    elif(answer==4):
        search1()
    elif(answer==5):
        quit()
    else:
        print("输入错误！请重新输入！")
        menu()
if __name__ == '__main__':
    menu()
