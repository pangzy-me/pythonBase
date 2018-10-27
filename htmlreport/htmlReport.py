# HTMLTestRunner.py文件放在\Python\Lib\ 目录下
# 需在命令行执行才能生成测试报告文档，unittest执行无效果。
# E:\Python_Test\aTest\htmlreport>python htmlReport.py

print('------开始生成HTML测试报告------')

import unittest
import HTMLTestRunner
# import time

def add(a,b):
	return a+b


class TestMathFunc(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, add(1, 4))

    def test2(self):
        self.assertEqual(5, add(1, 4))

    def test3(self):
        self.assertEqual(5, add(1, 4))

    def test4(self):
        self.assertEqual(5, add(1, 4))

    def test5(self):
        self.assertEqual(5, add(1, 4))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMathFunc("test1"))
    suite.addTest(TestMathFunc("test2"))
    suite.addTest(TestMathFunc("test3"))
    suite.addTest(TestMathFunc("test4"))
    suite.addTest(TestMathFunc("test5"))
    # 简单使用时间标记
    # now = time.strftime("%Y-%m-%d %H:%M:%S")  ## 时间打印格式是正确的，但是文件名不能使用冒号
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # 定义生成的HTML报告文档名称及存放路径
    filepath = 'E:\\Python_Test\\aTest\\htmlreport\\testReport.html'
    fp = open(filepath, 'wb')
    # 定义报告的属性值
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='HTML测试报告',description='用例执行结果')
    runner.run(suite)
    unittest.main()
    fp.close()
