#coding=gbk

from random import randint
class Dice:
    """������"""
    def __init__(self, num_sides=6):
        """����Ĭ��Ϊ6����"""
        self.num_sides = num_sides
    def roll(self):
        """"����λ��1����������֮������ֵ"""
        return randint(1, self.num_sides)
