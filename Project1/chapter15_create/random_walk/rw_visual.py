#coding=gbk
#只要程序处于活跃状态，就不断随机漫步

import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    #创建RandomWalk实例
    rw = RandomWalk(50000)
    rw.fill_walk()
    #绘制所有点
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))#调整尺寸以适合屏幕
    point_numbers = range(rw.num_points)#生成数字列表(长度与随机漫步的数量相同)
    #设置颜色映射,edgecolors='none'删除每个点周围的轮廓
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=1)

    #突出显示起点和终点，起点标绿色，终点标红色
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)

    #隐藏坐标
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("是否重新进行随机漫步? (y/n): ")
    if keep_running == 'n':
        break
