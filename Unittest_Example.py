import unittest

def div(a, b):
    return a // b

class MyfirstTestCase(unittest.TestCase):
    def setUp(self):
        print('run before every test')

    def test_1_div_1(self):
        print('1 div 1')
        self.assertEquals(div(1, 1), 1 // 1)

    def test_3_div_4(self):
        print('3 div 4')
        self.assertEquals(div(3, 4), 3 // 4)

    def test_3_div_0(self):
        print('3 div 0')
        self.assertRaises(ZeroDivisionError, div, 3, 0)  # 当程序代码运行到div，执行3//0的时候，就会抛出一个ZeroDivisionError异常

    def tearDown(self):
        print('run after every test')

if __name__ == '__main__':
    unittest.main()
