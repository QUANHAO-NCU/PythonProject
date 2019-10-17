
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'test module,测试if __name__ = __main__的作用'

__author__ = 'QH'

# test0
print('直接在本程序调用这个模块则会显示这句话！')

def test1():
    print('在其他Python文件里调用这个模块则会显示这句话！')

if __name__ != '__main__':
    test1()