#coding=gbk
import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    """����dice.py�ļ��е�Dice��"""
    def setUp(self):
        """����һ��9���Dice����"""
        self.dice=Dice(9)
    def test_roll_01(self):
        """����Ͷ��һ�����ӣ������Ƿ���1~9֮�䣨����1��9��"""
        result=self.dice.roll()
        self.assertIn(result,range(1,10))
    def test_roll_02(self):
        """����Ͷ��һ�����ӣ������Ƿ���1~9֮�䣨����1��9��"""
        result=self.dice.roll()
        self.assertNotIn(result,range(1,10))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()