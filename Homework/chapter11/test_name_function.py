import unittest
from name_function import *
class NameTest(unittest.TestCase):
    def test_name(self):
        name=get_name("Long","Shaoqing")
        self.assertEqual(name,"Long Shaoqing")
if __name__ == '__main__':
    unittest.main