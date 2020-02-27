#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
编写者：XZY
日期：2020.02.26
功能：筛选1000以内的阿姆斯特朗数
注：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
"""

n = 1
for x in range(1,1000):
    a = 0
    for i in range(len(str(x))):
        a = a + int(str(x)[i])**len(str(x))
    if a == x:
        print(f'第{n}个阿姆斯特朗数为：{x}')
        n += 1
