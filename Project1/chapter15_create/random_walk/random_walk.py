#coding=gbk

"""随机漫步"""
import matplotlib.pyplot as plt
from random import choice
class RandomWalk:
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        #所有随机漫步都开始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步的所有点"""
        #随机漫步，直到列表到达指定长度
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])#随机选择x轴前进的方向
            x_distance = choice([0, 1, 2, 3, 4])#随机选择x轴前进的距离
            x_step = x_direction * x_distance #x轴方向前进的距离
        
            y_direction = choice([1, -1])#随机选择y轴前进的方向
            y_distance = choice([0, 1, 2, 3, 4])#随机选择y轴前进的距离
            y_step = y_direction * y_distance #y轴方向前进的距离
        
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
        
            #计算下一个点的x,y值
            x = self.x_values[-1] + x_step #x列表最后一个值 + x_step
            y = self.y_values[-1] + y_step #y列表最后一个值 + y_step

            #将x,y添加到表的末尾
            self.x_values.append(x)
            self.y_values.append(y)

# if __name__ == '__main__':
#     # 创建RandomWalk实例
#     rw = RandomWalk()
#     rw.fill_walk()
#     plt.style.use("classic")
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     plt.show()

