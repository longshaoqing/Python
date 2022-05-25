#coding=gbk
import unittest
from dice import Dice

class TestDice(unittest.TestCase):
    def setUp(self):
        self.dice=Dice(9)
    def test_roll_01(self):
        result=self.dice.roll()
        self.assertIn(result,range(1,9))
    def test_roll_02(self):
        result=self.dice.roll()
        self.assertIn(result,range(9,100))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()