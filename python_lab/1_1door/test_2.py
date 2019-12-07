#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:55:50 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

题目1: 打印1~10的数字以及每个数的平方、几何级数和阶乘

"""
from math import factorial
def main():
    print('%-10s%-10s%-10s%-10s' % ('数字', '平方','几何级数', '阶乘'))
    #-表示左对齐，+表示在转换值之前要加上正负号；“”（空白字符）表示正数之前保留空格；0表示转换值若位数不够则用0填充
    #%字符：标记转换说明符的开始
    for num in range(1, 11):
        print('%-12d%-12d%-12d%-12d' % (num, num ** 2, 2 ** num, factorial(num)))

if __name__ == '__main__':
    main()
