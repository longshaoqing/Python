#coding=gbk
import unittest,json
from eq_explore_data import append

class TestAppendFunction(unittest.TestCase):
    """测试eq_explore_data文件中的append()函数"""
    def setUp(self):
        """提取与键features相关联的文件数据"""
        filename = 'data/eq_data_30_day_m1.json'
        with open(filename) as f:
            all_eq_data = json.load(f)  # json.load()将数据转换为Python能够处理的格式
        self.all_eq_dicts = all_eq_data['features']  # 提取与键features相关联的数据
    def test_append_mags(self):
        """测试是否将震级存储在properties的mag键下，存储到mags[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(mags[3],3.6)
    def test_append_titles(self):
        """测试是否将位置存储在properties的title键下，存储到titles[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(titles[0],"M 1.0 - 8km NE of Aguanga, CA")
    def test_append_lons(self):
        """测试是否将纬度存储在properties的coordinates键下标为0的位置，存储到lons[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(lons[1],-148.9865)
    def test_append_lats(self):
        """测试是否将经度存储在properties的coordinates键下标为1的位置，存储到lats[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(lats[2],-12.1025)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()