#coding=gbk

"""�������"""
import matplotlib.pyplot as plt
from random import choice
class RandomWalk:
    def __init__(self, num_points=5000):
        """��ʼ���������������"""
        self.num_points = num_points
        #���������������ʼ�ڣ�0,0��
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """����������������е�"""
        #���������ֱ���б���ָ������
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])#���ѡ��x��ǰ���ķ���
            x_distance = choice([0, 1, 2, 3, 4])#���ѡ��x��ǰ���ľ���
            x_step = x_direction * x_distance #x�᷽��ǰ���ľ���
        
            y_direction = choice([1, -1])#���ѡ��y��ǰ���ķ���
            y_distance = choice([0, 1, 2, 3, 4])#���ѡ��y��ǰ���ľ���
            y_step = y_direction * y_distance #y�᷽��ǰ���ľ���
        
            #�ܾ�ԭ��̤��
            if x_step == 0 and y_step == 0:
                continue
        
            #������һ�����x,yֵ
            x = self.x_values[-1] + x_step #x�б����һ��ֵ + x_step
            y = self.y_values[-1] + y_step #y�б����һ��ֵ + y_step

            #��x,y��ӵ����ĩβ
            self.x_values.append(x)
            self.y_values.append(y)

# if __name__ == '__main__':
#     # ����RandomWalkʵ��
#     rw = RandomWalk()
#     rw.fill_walk()
#     plt.style.use("classic")
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()

