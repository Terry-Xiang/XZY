#!usr/bin/python3
# -*- coding: utf-8 -*-
"""
编写者：XZY
日期：2020.2.17
功能：输出九九乘法表
"""

y=1
L=[1,2,3,4,5,6,7,8,9]
for x in L:
    if x <= y:
        print('x*y=',x*y)
    else:
        y=y+1    