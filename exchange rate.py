#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
编者：XZY
日期：2020.2.15
功能：实现美元与人民币汇率转换
"""

#提示用户输入基本信息
print('美元货币单位是USD，人民币的货币单位是CNY')
print('汇率为直接标价法，CNY/USD，其含义为 1 美元 = ？人民币')
print('汇率查询参考网站：https://www.boc.cn/sourcedb/whpj/')
print('请注意大小写')
exchange_rate = input('请输入今日汇率：') #汇率标价为 CNY/USD
currency = input('请输入带有货币单位的金额：')

#转换汇率
if currency[-3:] == 'CNY':
    Dollar = eval(currency[:3]) / eval(exchange_rate)
    print(currency[:3] + '人民币' + '相当于' + str(Dollar) + '美元')
elif currency[-3:] == 'USD':
    RMB = eval(currency[:3]) * eval(exchange_rate)
    print(currency[:3] + '美元' + '相当于' + str(RMB) + '人民币')
else:
    print('输入格式错误，请重新输入')
    