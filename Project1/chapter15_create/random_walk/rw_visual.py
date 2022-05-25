#coding=gbk
#ֻҪ�����ڻ�Ծ״̬���Ͳ����������

import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    #����RandomWalkʵ��
    rw = RandomWalk(50000)
    rw.fill_walk()
    #�������е�
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))#�����ߴ����ʺ���Ļ
    point_numbers = range(rw.num_points)#���������б�(���������������������ͬ)
    #������ɫӳ��,edgecolors='none'ɾ��ÿ������Χ������
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=1)

    #ͻ����ʾ�����յ㣬������ɫ���յ���ɫ
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)

    #��������
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("�Ƿ����½����������? (y/n): ")
    if keep_running == 'n':
        break
