#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
编写者：XZY
日期：2020.2.15
功能：求一元二次方程的解
"""

# 提示使用者输入一元二次方程的三个系数
print('解ax**2+bx+c=0的根')
a = float(input('请输入a的值：'))
b = float(input('请输入b的值：'))
c = float(input('请输入c的值：'))
# 解方程过程
import math
def quadratic(a, b, c):     #构造求根函数
    delta = b*b-4*a*c       #delta即一元二次方程根的判别式
    if a == 0 and b == 0:   #判断是否为方程
        return print('该方程不成立')
    elif a == 0 and b != 0: #判断方程是否为一元一次方程
        x = -c/b
        return print('该方程为一元一次方程，其根为','x=',x)
    elif delta > 0:         #判别式大于零的情况
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        return print('该方程的根为','x1=',x1,' x2=',x2)
    elif delta == 0:        #判别式等于零的情况
        x = -b/(2*a)
        return print('该方程的根为','x=',x)
    else:
	    return print('该方程没有实根')
quadratic(a,b,c)
