#coding=gbk
import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    """测试dice.py文件中的Dice类"""
    def setUp(self):
        """创建一个9面的Dice对象"""
        self.dice=Dice(9)
    def test_roll_01(self):
        """测试投掷一个骰子，点数是否在1~9之间（包括1和9）"""
        result=self.dice.roll()
        self.assertIn(result,range(1,10))
    def test_roll_02(self):
        """测试投掷一个骰子，点数是否不在1~9之间（包括1和9）"""
        result=self.dice.roll()
        self.assertNotIn(result,range(1,10))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()