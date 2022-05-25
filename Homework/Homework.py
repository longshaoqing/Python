# foods=["apple","rice","banana","cake","pizza"]
# for food in foods:
#     print(food)
# for food in foods:
#     print("I like "+food+".")
#
# lists=["The","first","three","items","in","the","list", "are:"]
# print(lists)
# print(lists[:3])
#
# lists=["Three","items","from","the","middle","of","the","list", "are:"]
# print(lists)
# print(lists[3:6])
#
# lists=["The","last","three","items","in","the","list", "are:"]
# print(lists)
# print(lists[-3:])
#
# numbers=list(range(1,10))
# print(numbers)
# for number in numbers:
#     if(str(number)=="1"):
#         print("1st")
#     elif(str(number)=="2"):
#         print("2nd")
#     elif(str(number)=="3"):
#         print("3rd")
#     else:
#         print(str(number)+"th")
#
# words = ['cat', 'window', 'defenestrate', 'apple', 'dog', 'is', 'the', 'best']
# Word=[word.title() for word in words if len(word)>=5]
# print(Word)
#
# print("Sakyamuni once said, \"No matter who you meet, he is the person in your life, not by chance, he will teach you something\".")
#
# famous_person="Sakyamuni"
# message="\"No matter who you meet, he is the person in your life, not by chance, he will teach you something\"."
# print(famous_person+" once said,"+message)
#
# name="Sakyamuni\t\t"
# name2="\nSakyamuni"
# print(name2.lstrip())
# print(name.rstrip())
#
# lists=["湘哥","米子哥","陈毅"]
# print(lists)
# print("因"+lists[0]+"无法赴约,我重新邀请了龙少")
# lists[0]="龙少"
# print(lists)
#
# print("我找到了一个更大的餐桌，想再邀请3位嘉宾")
# lists.insert(0,"齐老板")
# lists.insert(2,"华子哥")
# lists.append("小米")
# print(lists)
# print(len(lists))
#
# print("\n刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾共进晚餐")
# print(lists)
# while len(lists)>2:
#     print("很抱歉，无法邀请您("+lists.pop()+")来共进晚餐！")
# for name in lists:
#     print("欢迎与您("+name+")在洪山大酒店共进晚餐！")
#
# while len(lists)>0:
#     del lists[len(lists)-1]
# # del lists[1]
# # del lists[0]
# print(lists)
#
# places=["beijing","shanghai","changsha","zhuhai","aomen"]
# print(places)
# print(sorted(places))
# print(places)
# print("\n")
# print(sorted(places,reverse=True))
# print(places)
#
# print("\n")
# places.reverse()
# print(places)
# places.reverse()
# print(places)
# print("\n")
#
# places.sort()
# print(places)
# places.sort(reverse=True)
# print(places)
#

#------------------------------------------------------------------

# lists=["banana pizza","watermelon pizza","orange pizza"]
# for i in range(0,3):
#     print(f"I like {lists[i]}.")
# print("I really love pizza!")
#
# animals=["dog","pig","cat"]
# for i in range(0,3):
#     print(f"A {animals[i]} would make a great pet.")
# print("Any of these animals would make a great pet!")
#
# print([i**3 for i in range(1,11)])
# print([i**3 for i in range(1,11) if i%2==0])
# print([i**3 for i in range(1,11) if i**3<=100])
# lists=["Three","items","from","the","middle","of","the","list", "are:"]
# print(lists)
# print(lists[int((len(lists)/2)-1):int((len(lists)/2)+2)])
# lists=["The","first","three","items","in","the","list", "are:"]
# print(lists[-1:1:-1])


# lists=["The","first","three","items","in","the","list", "are:"]
# print(lists[-1:-7:-1])
#
# lists=["banana pizza","watermelon pizza","orange pizza"]
# friend_pizzas=lists[:]
# lists.append("apple pizza")
# friend_pizzas.append("strawberry pizza")
# print("My favorite pizzas are:")
# for i in range(0,len(lists)):
#     print(lists[i])
# print("My friend's favorite pizzas are:")
# for i in range(0,len(friend_pizzas)):
#     print(friend_pizzas[i])
#
# my_foods=["pizza","falafel","carrot cake"]
# for i in my_foods:
#     print(i)
# for i in range(0,len(my_foods)):
#     print(my_foods[i])
#
# foods=("pork","rice","beef","chicken","vegetable")
# for i in foods:
#     print(i)


# def describe_city(city,country="中国"):
#     print(f"{city}属于{country}")
# describe_city("北京")
# describe_city("东京","日本")


# numbers=list(range(1,10))
# print(numbers)
# for number in numbers:
#     if(str(number)=="1"):
#         print("1st")
#     elif(str(number)=="2"):
#         print("2nd")
#     elif(str(number)=="3"):
#         print("3rd")
#     else:
#         print(str(number)+"th")
#
# person={"first_name":"海滨","last_name":"米","age":"20","city":"长沙"}
# print("姓名："+person["last_name"]+person["first_name"]+"\n"+"年龄:"+person["age"]+"\n"+"城市:"+person["city"])
#
# numbers={"米子哥":20,"湘哥":13,"龙少":313,"罗董":25,"齐老板":33}
# number={}
# keys=numbers.keys()
# for i in keys:
#     if(numbers[i]%2!=0):
#         number[i]=str(numbers[i])
# print(number)
#
#
# terms={"列表":"列表就是列表","元组":"元组就是元组","字典":"字典就是字典","集合":"集合就是集合","函数":"函数就是函数"}
# keys=terms.keys()
# for i in keys:
#     print(i+":"+terms[i])
# print()
# terms["循环"]="循环就是循环"
# terms["遍历"]="遍历就是遍历"
# terms["if语句"]="if语句就是if语句"
# terms["异常"]="异常就是异常"
# terms["字符串"]="字符串就是字符串"
# keys=terms.keys()
# for i in keys:
#     print(i+":"+terms[i])
#
#
#
#
#
# numbers={"米子哥":[20,13,341,52],"湘哥":[13,51,135,2624,647],"龙少":[313,35,57,78,95],"罗董":[25,35,12],"齐老板":[33,94]}
# for name,number in numbers.items():
#     print(name+"喜欢的数字有：")
#     for i in number:
#         print(str(i),end=" ")
#     print()
#
# numbers=[str(x)+"st" if x==1
#          else str(x)+"nd" if x==2
#          else str(x)+"rd" if x==3
#          else str(x)+"th"
#          for x in range(1,11)]
# print(numbers)


# numbers={"米子哥":20,"湘哥":13,"龙少":313,"罗董":25,"齐老板":33}
# number={k:v for k,v in numbers.items() if v%2!=0}
# print(number)

# 7-2
# person=input("请问有多少人就餐？")
# if int(person)>8:
#     print("没有空桌")
# else:
#     print("有空桌")

# while(1):
#     x=input("请输入一系列披萨配料：")
#     if x=="quit":
#         break
#     print("我们会在披萨中放入\"" + x + "\"配料")

# while(1):
#     x=input("你多大年龄?")
#     if x=="-1":
#         break
#     if int(x)<0:
#         print("请重新输入正确的年龄！")
#         continue
#     if int(x)<3:
#         print("免费")
#     elif int(x)<12:
#         print("收费$10")
#     else:
#         print("收费$15")

# #字典生成式 用zip()
# items=["fruits","books","others"]
# prices=[12,13,14]
# d={items:prices for items,prices in zip(items,prices)}
# print(d)

# # 7-6
# #active控制循环
# active = True
# while active:
#     x = input("请输入披萨的配料：")
#     if x == 'quit':
#         active = False
#     else:
#         print("我们会在披萨中放入\"" + x + "\"配料")

# sandwich_order=["草莓三明治","牛肉三明治","冰激凌三明治"]
# finished_sandwich=[]
# for i in sandwich_order:
#     print("我制作了"+i)
#     finished_sandwich.append(i)
# print("\n已经制作好了的三明治有：")
# print(finished_sandwich)

# sandwich_order=["草莓三明治","牛肉三明治","冰激凌三明治"]
# finished_sandwich=[]
# sandwich_order.insert(0,"pastrami")
# sandwich_order.insert(2,"pastrami")
# sandwich_order.insert(4,"pastrami")
# for i in sandwich_order:
#     finished_sandwich.append(i)
# print("\n已经制作好了的三明治有：")
# print(finished_sandwich)
# print("pastrami已经卖完了")
# while (1):
#     if "pastrami" in finished_sandwich:
#         finished_sandwich.remove("pastrami")
#     else:
#         break
# print(finished_sandwich)

# 创建一个包含年龄范围（range对象）的列表和一个电影票价的列表，利用zip函数生成一个（年龄范围，电影票价）元组的列表。
# 然后利用这个元组列表来判断某个年龄的电影票价。
# age=[range(0,4),range(4,13),range(13,120)]
# price=[0,10,15]
# Zip=(zip(age,price))
# Age=int(input("请输入年龄："))
# for age,price in Zip:
#     if Age in age:
#         print("你需要支付"+str(price)+"美元")

# 编写一个循环，要求用户输入他们的姓名和收入，然后使用字典保存用户输入的数据（至少保存5个用户的数据），遍历字典打印用户的收入。
# 然后使用列表推导，找到所有收入大于10000的用户，使用元组列表保存用户姓名和用户的收入。
# salarys=[]
# for i in range(0,5):
#     name=input("输入姓名：")
#     salary=int(input("输入收入："))
#     salarys.append({"name":name,"salary":salary})
# print(salarys)
# print("所有收入大于10000的用户:")
# output=[income for income in salarys if income["salary"]>10000]
# print(output)

# 使用一行嵌套列表的推导创建一个嵌套列表，嵌套列表包含每行文本的单词长度大于3的单词列表
# （如果有6行文本，就会有6个单词列表放入到一个嵌套列表中）。
# text = '''Call me Ishmael. Some years ago - never mind how long precisely – having
# little or no money in my purse, and nothing particular to interest me
# on shore, I thought I would sail about a little and see the watery part
# of the world. It is a way I have of driving off the spleen, and
# regulating
# the circulation. - Moby Dick'''
#
# words = [[word for word in line.split() if len(word) > 3] for line in text.split("\n")]
# print(words)

# 列表切片的使用
# price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
#          [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
#          [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
#          [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
# new_prices = [line[::2] for line in price]
# print(new_prices)

# 使用切片修复残缺的数据
# visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
#             'Safari', 'corrupted', 'Safari', 'corrupted',
#             'Chrome', 'corrupted', 'Firefox', 'corrupted']
# visitors[1::2] = visitors[::2]
# print(visitors)

# column_names = ['name', 'salary', 'job']
# db_rows = [('Alice', 180000, 'data scientist'),
#            ('Bob', 99000, 'mid-level manager'),
#            ('Frank', 87000, 'CEO')]
# values = [dict(zip(column_names, row)) for row in db_rows]
# print(values)

# 练习8-1：消息 　编写一个名为display_message() 的函数，它打印一个句子，指出你在本章学的是什么。
# 调用这个函数，确认显示的消息正确无误。
# def display_message():
#     print("我本章学习了对函数的调用")
# display_message()

# 练习8-3：T恤 　编写一个名为make_shirt() 的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应打印一个句子，概要地说明T恤的尺码和字样。使用位置实参调用该函数来制作一件T恤，再使用关键字实参来调用这个函数。
# def make_shirt(size,words):
#     print("这件衣服的尺码是："+size+"，T恤上的字样是："+words)
# make_shirt("XL","Just do it")
# make_shirt(size="L",words="中国李宁")

# 练习8-4：大号T恤 　修改函数make_shirt() ，使其在默认情况下制作一件印有“I love Python”字样的大号T恤。
# 调用这个函数来制作：一件印有默认字样的大号T恤，一件印有默认字样的中号T恤，以及一件印有其他字样的T恤（尺码无关紧要）。
# def make_shirt(size,words="I love Python"):
#     print("这件衣服的尺码是："+size+"，T恤上的字样是："+words)
# make_shirt("XXL")
# make_shirt("L")
# make_shirt("S","中国李宁")

# 练习8-7：专辑 　编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给函数make_album() 添加一个默认值为None 的可选形参，以便存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将该值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# def make_album(name,album,number=None):
#     if number:
#         return {"name":name,"album":album,"number":number}
#     else:
#         return {"name":name,"album":album}
# print(make_album("周杰伦","周杰伦专辑",9))
# print(make_album("王靖雯","王靖雯专辑"))
# print(make_album("薛之谦","薛之谦专辑",6))

# 练习8-8：用户的专辑 　在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album() 并将创建的字典打印出来。在这个while 循环中，务必提供退出途径。
# def make_album(name,album,number=None):
#     if number:
#         return {"name":name,"album":album,"number":number}
#     else:
#         return {"name":name,"album":album}
# while True:
#     name=input("请输入歌手名称：")
#     if name == "-1":
#         break
#     album=input("请输入专辑名称：")
#     print(make_album(name,album))

# 练习8-9：消息创建一个列表，其中包含一系列简短的文本消息。将该列表传递给一个名为show_messages() 的函数，
# 这个函数会打印列表中的每条文本消息。
# def show_messages(words):
#     for word in words:
#         print(word)
# show_messages(["我要","飞得","更高"])

# 练习8-10：发送消息 　在你为完成练习8-9而编写的程序中，编写一个名为send_messages() 的函数，
# 将每条消息都打印出来并移到一个名为sent_messages 的列表中。
# 调用函数send_messages() ，再将两个列表都打印出来，确认正确地移动了消息。
# sent_messages=[]
# def send_messages(word):
#     print(word)
#     sent_messages.append(word)
# def show_messages(words):
#     while words:
#         send_messages(words.pop())
# words=["我要","飞得","更高"]
# show_messages(words)
# print(words)
# print(sent_messages)

# 练习8-11：消息归档 　修改你为完成练习8-10而编写的程序，在调用函数send_messages() 时，
# 向它传递消息列表的副本。调用函数send_messages() 后，将两个列表都打印出来，确认保留了原始列表中的消息。
# sent_messages=[]
# def send_messages(word):
#     print(word)
#     sent_messages.append(word)
# def show_messages(words):
#     for word in words:
#         send_messages(word)
# words=["我要","飞得","更高"]
# show_messages(words)
# print(words)
# print(sent_messages)
#
# 练习8-14：汽车 　编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 这样调用该函数：提供必不可少的信息，以及两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
# def make_car(maker,model,**cars):
#     cars["maker"]=maker
#     cars["model"]=model
#     return cars
# print(make_car('subaru', 'outback', color='blue', tow_package=True))

# 练习8-16：导入 选择一个你编写的且只包含一个函数的程序，将该函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# module_name.function_name()
# from module_name import function_name
# function_name()
# from module_name import function_name as fn
# fn()
# import module_name as mn
# mn.function_name()
# from module_name import *
# function_name()

# 编写一个Lambda函数，函数的输入参数为一个小于1000的整数，返回值为该整数各位数字的和。
# 然后利用该Lambda函数对一组小于1000的整数列表进行排序。
# number=int(input("请输入一个数："))
# def add(number):
#     one=number//100
#     two=number//10%10
#     three=number%10
#     return one+two+three
# print(add(number))
#
# lists=[989,123,456,789]
# lists.sort(key=add)
# print(lists)
# print(list(map(lambda x:x**2+1,lists)))

#附加题3
# companies = {
# 'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
# 'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
# 'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
# illegal=[company for company in companies if any(salary<9 for salary in companies[company].values())]
# print(illegal)


# 练习9-1：餐馆 　创建一个名为Restaurant 的类，为其方法__init__()设置属性restaurant_name 和cuisine_type 。
# 创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，前者打印前述两项信息，而后者打印一条消息，
# 指出餐馆正在营业。根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#     def describe_restaurant(self):
#         print("餐馆名为："+self.restaurant_name+"\t菜式为："+self.cuisine_type)
#     def open_restaurant(self):
#         print("餐馆正在营业")
# restaurant=Restaurant("老北京菜馆","北京菜")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# 练习9-4：就餐人数 　在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant 的实例。打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
    def describe_restaurant(self):
        print("餐馆名为："+self.restaurant_name+"\t菜式为："+self.cuisine_type+"\t在这家餐馆就过餐的人数有："+str(self.number_served))
    def open_restaurant(self):
        print("餐馆正在营业")
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,numbers):
        self.number_served+=numbers
# restaurant=Restaurant("老北京菜馆","北京菜")
# restaurant.describe_restaurant()
# restaurant.set_number_served(300)
# restaurant.describe_restaurant()
# restaurant.increment_number_served(700)
# restaurant.describe_restaurant()

# 附加题：创建至少包含5个餐馆对象的列表：
# 	找到列表中就餐人数最多的餐馆。
# 	利用列表解析，找到这些餐馆中就餐人数大于等于10的餐馆。
# 	统计列表中所有餐馆就餐人数的总和。
# restaurant1=Restaurant("老北京菜馆","北京菜",320)
# restaurant2=Restaurant("上海菜馆","上海菜",200)
# restaurant3=Restaurant("湖南菜馆","湘菜",500)
# restaurant4=Restaurant("广东菜馆","粤菜",450)
# restaurant5=Restaurant("天津菜馆","天津菜",333)
# restaurant_list=[restaurant1,restaurant2,restaurant3,restaurant4,restaurant5]
# 	找到列表中就餐人数最多的餐馆。
# Max = 0
# for i in range(0,len(restaurant_list)):
#     if int(restaurant_list[i].number_served)>Max:
#         Max=int(restaurant_list[i].number_served)
# for i in range(0,len(restaurant_list)):
#     if int(restaurant_list[i].number_served)==Max:
#         print(restaurant_list[i].restaurant_name)

# 	利用列表解析，找到这些餐馆中就餐人数大于等于10的餐馆。
# res_list=[res for res in restaurant_list if res.number_served>10]
# for it in res_list:
#     it.describe_restaurant()
# 	统计列表中所有餐馆就餐人数的总和
# Sum = 0
# for i in range(0,len(restaurant_list)):
#     Sum+=int(restaurant_list[i].number_served)
# print(Sum)

# 练习9-6：冰激凌小店 　冰激凌小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，
# 让它继承为完成练习9-1或练习9-4而编写的Restaurant 类。
# 这两个版本的Restaurant 类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors 的属性，用于存储一个由各种口味的冰激凌组成的列表。
# 编写一个显示这些冰激凌的方法。创建一个IceCreamStand 实例，并调用这个方法。
# class IceCreamStand(Restaurant):
#     def __init__(self):
#         self.flavors=["草莓味","巧克力味","西瓜味"]
#     def show(self):
#         print(self.flavors)
# iceCreamStand=IceCreamStand()
# iceCreamStand.show()


# 练习9-13：骰子 　创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一个名为roll_die() 的方法，
# 它打印位于1和骰子面数之间的随机数。创建一个6面的骰子再掷10次。
# 创建一个10面的骰子和一个20面的骰子，再分别掷10次。
# from random import*
# class Die:
#     def __init__(self,sides=6):
#         self.sides=sides
#     def roll_die(self):
#         print(randint(1,self.sides),end=" ")
# die10=Die(10)
# for i in range(0,10):
#     die10.roll_die()
# print()
# die20=Die(20)
# for i in range(0,10):
#     die20.roll_die()

# 练习9-14：彩票 　创建一个列表或元组，其中包含10个数和5个字母。
# 从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。
# from random import*
# lottery=["1","2","3","4","5","6","7","8","9","10","a","l","s","q","m"]
# strings=""
# lotterys=choices(lottery,k=4)
# print("只要彩票上是:"+str(lotterys)+"，就中大奖了！")

# 练习9-15：彩票分析 　可以使用一个循环来明白前述彩票大奖有多难中奖。
# 为此，创建一个名为my_ticket 的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
# 请打印一条消息，报告执行循环多少次才中了大奖。
# Sum=0
# while(1):
#     my_ticket=choices(lottery, k=4)
#     if my_ticket==lotterys:
#         break
#     else:
#         Sum+=1
# print("报告执行循环"+str(Sum)+"次才中了大奖")

# 附加题： 创建一个Money类，包括至少两个属性面值（amount）和币种(currency), 为这个类编写__str__函数，
# 使得Money对象被打印时可以显示Money对象的面值和币种，重载Money类的操作符，使得Money对象可以直接使用+, -, *, /， ==， >, <
# 这些操作符。（注意：两个Money对象使用这些操作时，需要先判断他们的币种）
# class Money:
#     def __init__(self,amount,currency):
#         self.amount=amount
#         self.curency=currency
#     def __str__(self):
#         print("面值为："+str(self.amount)+",币种为："+self.curency)
#     def __add__(self, other):
#         if self.curency==other.curency:
#             return self.amount+other.amount
#     def __sub__(self, other):
#         if self.curency == other.curency:
#             return self.amount - other.amount
#     def __mul__(self, other):
#         return self.amount*other.amount
#     def __truediv__(self, other):
#         return self.amount / other.amount
#     def __eq__(self, other):
#         return self.amount==other.amount
#     def __gt__(self, other):
#         return self.amount>other.amount
#     def __lt__(self, other):
#         return self.amount < other.amount
#
# money1=Money(300,"RMB")
# money2=Money(200,"RMB")
# money3=Money(100,"Dollar")
# SUM=money1+money3
# print(SUM)
# SUB=money1-money2
# print(SUB)
# MUL=money1*money2
# print(MUL)


# 附加题：从dataclasses导入dataclass，使用dataclass来创建Money类，并实现上面同样的功能。
# from dataclasses import dataclass
# @dataclass(init=True, repr=True, eq=True)
# class Money():
#     amount:int
#     currency:str
#     def __str__(self) -> str:
#         return '(Money: %s, %s)' % (self.amount, self.currency)
#     def __add__(self, other):
#         return Money(self.amount + other.amount,self.currency)
#     def __sub__(self, other):
#         return Money(self.amount - other.amount, self.currency)
#     def __mul__(self, other):
#         return Money(self.amount * other.amount, self.currency)
#     def __truediv__(self, other):
#         return Money(self.amount / other.amount, self.currency)
#     def __eq__(self, other) -> bool:
#         return self.amount==other.amount
#     def __gt__(self, other) -> bool:
#         return self.amount>other.amount
#     def __lt__(self, other) -> bool:
#         return self.amount < other.amount
# if __name__=='__main__':
#     money1=Money(100,'人民币')
#     money2=Money(300,'人民币')
#     if money1>money2:
#         print("money1")
#     else:
#         print("money2")
#     money=money1*money2
#     print(money)


# 练习10-1：Python学习笔记 　在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，
# 其中每一行都以“In Python you can”打头。将这个文件命名为learning_python.txt，
# 并存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，并将你所写的内容打印三次：
# 第一次打印时读取整个文件；第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with 代码块外打印它们。
# print("第1次打印：")
# with open("learning_python.txt","r")as file1:
#     print(file1.read())
# print("第2次打印：")
# with open("learning_python.txt","r")as file1:
#     for line in file1:
#         print(line.rstrip())
# print("第3次打印：")
# s=[]
# with open("learning_python.txt","r")as file1:
#     for line in file1:
#         s.append(line)
# print(s)

# 练习10-3：访客 　编写一个程序，提示用户输入名字。用户做出响应后，将其名字写入文件guest.txt中。
# with open("guest_book.txt","a")as file1:
#     while(1):
#         name = input("请输入用户名：")
#         if name=="q":
#             break
#         if name!='':
#             print("欢迎"+name+"先生(女士)访问")
#             file1.write(name+"访问"+"\n")

# 练习10-6：加法运算 　提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
# 在此情况下，当你尝试将输入转换为整数时，将引发ValueError 异常。编写一个程序，提示用户输入两个数，再将其相加并打印结果。
# 在用户输入的任何一个值不是数时都捕获ValueError 异常，并打印一条友好的错误消息。
# 对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。
# if __name__ == '__main__':
#     try:
#         number1=int(input("请输入第1个数："))
#         number2=int(input("请输入第2个数："))
#         result=number1+number2
#         print(str(number1)+"+"+str(number2)+"="+str(result))
#     except ValueError:
#         print("输入错误！请输入数值！")

# 练习10-7：加法计算器 　将为完成练习10-6而编写的代码放在一个while 循环中，让用户犯错（输入的是文本而不是数）后能够继续输入数。
# if __name__ == '__main__':
#     while(1):
#         try:
#             number1=int(input("请输入第1个数："))
#             number2=int(input("请输入第2个数："))
#         except ValueError:
#             print("输入错误！请输入数值！")
#         else:
#             result = number1 + number2
#             print(str(number1) + "+" + str(number2) + "=" + str(result))

# 练习10-11：喜欢的数 　编写一个程序，提示用户输入喜欢的数，并使用json.dump() 将这个数存储到文件中。
# 再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
# I know your favorite number! It's _____.
# import json
# number=input("请输入你喜欢的一个数：")
# with open("test1.txt","w")as f:
#     json.dump(number,f)
#     f.write("\n")
# with open("test1.txt")as ff:
#     print(f"I know your favorite number! It's {json.load(ff)}.")

# 练习10-12：记住喜欢的数 　将练习10-11中的程序合二为一。如果存储了用户喜欢的数，就向用户显示它，
# 否则提示用户输入喜欢的数并将其存储到文件中。运行这个程序两次，看看它能否像预期的那样工作。
# import json
# try:
#     with open("test2.json")as f:
#         number=json.load(f)
# except FileNotFoundError:
#     number=input("请输入你喜欢的一个数：")
#     with open("test2.json","w")as f:
#         json.dump(number,f)
#         print("保存成功！")
# else:
#     print(f"I know your favorite number! It's {number}.")

# 附加题：编写一个程序，提示用户输入用户名和密码，使用字典保存用户名和密码，并保存到json格式的文件中，格式如下：
# {"username": "Mark", "password": "123456"}
# 再编写一个程序，从文件中读取用户名和密码，提示用户输入他的用户名和密码，如果用户名和密码正确，则提示用户登陆成功。
# 最后编写一个修改密码的程序，从文件中读取用户名和密码，用户首先必须正确输入原来的用户名和密码，
# 然后再输入新的密码，并且新的密码不能与旧密码相同。
# import json
# username_password={}
# def register():
#     print("注册!")
#     username=input("请输入用户名：")
#     password=input("请输入密码：")
#     username_password={"username": username, "password": password}
#     with open("test3.json","w")as f:
#         json.dump(username_password,f)
# def login():
#     print("登录!")
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     username_password = {"username": username, "password": password}
#     with open("test3.json")as f:
#         u_p=json.load(f)
#         if u_p==username_password:
#             print("登录成功！")
#             return True
#         else:
#             print("登录失败！")
#             return False
# def modify():
#     print("修改密码!")
#     print("请先登录！")
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     username_password = {"username": username, "password": password}
#     with open("test3.json") as f:
#         u_p = json.load(f)
#         if u_p == username_password:
#             print("登录成功！")
#             new_password=input("请输入新的密码：")
#             if new_password!=u_p["password"]:
#                 new_u_p={"username": username, "password": new_password}
#                 with open("test3.json","w")as ff:
#                     json.dump(new_u_p,ff)
#                 print("修改密码成功！")
#             else:
#                 print("新密码与原密码一致，修改失败！")
#         else:
#             print("登录失败！")
#
# if __name__ == '__main__':
#     modify()

# 附加题： 分析文本，从https://www.gutenberg.org/ebooks/11 下载《Alice in wonderland》,
# 统计在书中出现次数最多的7个英文单词是什么？ 再统计在长度大于等于5的英语单词中，出现最多的7个英文单词。
# with open("alice.txt",mode='r',encoding='UTF-8') as file_obj:
#     content=file_obj.read()
#
# symbol=[",",".",":","[","]","#","*","?","!","(",")",'“',"\n","/",'"','”']
# content=content.lower()
# for sy in symbol:
#     content=content.replace(sy," ")
# list_content=content.split()
# count={}
# for mes in list_content:
#     if mes not in count:
#         count[mes]=1
#     else:count[mes]+=1
# sort_count=dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
# cnt=0
# for key in sort_count:
#     if cnt==7:break
#     print(key+" "+str(count[key]))
#     cnt+=1

with open("alice.txt",mode='r',encoding='UTF-8') as file_obj:
    content=file_obj.read()

symbol=[",",".",":","[","]","#","*","?","!","(",")",'“',"\n","/",'"','”']
content=content.lower()
for sy in symbol:
    content=content.replace(sy," ")
list_content=content.split()
count={}
for mes in list_content:
    if len(mes)<5:continue
    if mes not in count:
        count[mes]=1
    else:count[mes]+=1
sort_count=dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
cnt=0
for key in sort_count:
    if cnt==7:break
    print(key+" "+str(count[key]))
    cnt+=1













