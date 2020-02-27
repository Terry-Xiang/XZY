#!/usr/bin/python3
#-*- coding:utf-8 -*-
"""
编者：XZY
日期：2020.2.15
功能：计算BMI
"""

print('BMI计算器')
print('依据BMI中国参考标准')
height=float(input('请输入你的身高(单位：厘米)：'))
weight=float(input('请输入你的体重（单位：千克）：'))
bmi = weight/(height*height/10000)
if bmi<18.5:
    print('你的BMI指数为:',bmi,'  属于 偏瘦')
elif 18.5<=bmi<23.9:
    print('你的BMI指数为:',bmi,'  属于 正常')
elif 23.9<=bmi<26.9:
    print('你的BMI指数为:',bmi,'  属于 偏胖')
elif 26.9<=bmi<29.9:
    print('你的BMI指数为:',bmi,'  属于 肥胖')
elif 29.9<=bmi<39.9:
    print('你的BMI指数为:',bmi,'  属于 重度肥胖')
else:
    print('你的BMI指数为:',bmi,'  属于 极重度肥胖')
