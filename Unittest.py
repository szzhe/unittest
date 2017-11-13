import unittest
import random

# 单元测试主要是对函数或是方法进行验证，检查是否符合预期

# 所有的用例都必须继承自unittest.TestCase
class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        print('before every test case')
        self.seq = range(10)

    # 在test类中，所有以test开头的方法都是测试用例
    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEquals(self.seq, range(10))

        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choise(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def tearDown(self):
        print('after every test case')


# 命令行中运行python your_test_file.py
if __name__ == '__main__':
    unittest.main()
