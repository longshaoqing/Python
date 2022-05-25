#coding=gbk

from random import randint
class Dice:
    """骰子类"""
    def __init__(self, num_sides=6):
        """骰子默认为6个面"""
        self.num_sides = num_sides
    def roll(self):
        """"返回位于1和骰子面数之间的随机值"""
        return randint(1, self.num_sides)
