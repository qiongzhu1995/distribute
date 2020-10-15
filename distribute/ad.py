#-*- coding: utf-8 -*-

# @ File     :distribute ad
# @ Author   ：lee
# @ Time     ：2020/10/15 20:04

class C(object):
    @staticmethod
    def f():
        print('runoob')


C.f()  # 静态方法无需实例化
cobj = C()
cobj.f()  # 也可以实例化后调用