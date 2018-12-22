'''
    爬虫
    断点调试快捷键：
        f5  启动程序
        f10 单步执行
        两次f5 从一个断点跳至另一个断点
        f11 跳转至函数/对象的内部执行

'''
from urllib import request

class Spider():
    url = 'https://www.panda.tv/cate/lol'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        temp = 0
    
    def go(self):
        self.__fetch_content()
    
spider = Spider()
spider.go()

