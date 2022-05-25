#coding=gbk
import unittest
from random_walk import RandomWalk

class TestDice(unittest.TestCase):
    def setUp(self):
        self.randomwalk=RandomWalk(5000)
        self.randomwalk.x_values=[0]
        self.randomwalk.y_values=[0]
    def test_randomwalk_01(self):
        walk = self.randomwalk.fill_walk()
        self.assertIn(walk, range(-4, 4))
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()