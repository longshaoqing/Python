#coding=gbk
import unittest,json
from eq_explore_data import append

class TestAppendFunction(unittest.TestCase):
    """����eq_explore_data�ļ��е�append()����"""
    def setUp(self):
        """��ȡ���features��������ļ�����"""
        filename = 'data/eq_data_30_day_m1.json'
        with open(filename) as f:
            all_eq_data = json.load(f)  # json.load()������ת��ΪPython�ܹ�����ĸ�ʽ
        self.all_eq_dicts = all_eq_data['features']  # ��ȡ���features�����������
    def test_append_mags(self):
        """�����Ƿ��𼶴洢��properties��mag���£��洢��mags[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(mags[3],3.6)
    def test_append_titles(self):
        """�����Ƿ�λ�ô洢��properties��title���£��洢��titles[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(titles[0],"M 1.0 - 8km NE of Aguanga, CA")
    def test_append_lons(self):
        """�����Ƿ�γ�ȴ洢��properties��coordinates���±�Ϊ0��λ�ã��洢��lons[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(lons[1],-148.9865)
    def test_append_lats(self):
        """�����Ƿ񽫾��ȴ洢��properties��coordinates���±�Ϊ1��λ�ã��洢��lats[]"""
        mags, titles, lons, lats = [], [], [], []
        append(mags, titles, lons, lats)
        self.assertEqual(lats[2],-12.1025)
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()