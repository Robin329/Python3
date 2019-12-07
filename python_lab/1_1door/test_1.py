#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:44:45 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""
题目1: 按照下面的格式打印1~10的数字以及每个数的平方、几何级数和阶乘

数字      平方      几何级数    阶乘
1       1       2       1
2       4       4       2
3       9       8       6
4       16      16      24
5       25      32      210
...

"""
def main():
    def factorial(n):
        """
        :param n:要求阶乘的数字
        :return:返回他的阶乘
        """
        if n == 1:
            return 1
        return n * factorial(n - 1)
    for x in range(1,11):
        print(x, x ** 2, 2 ** x, factorial(x))  #x ** 2:表示x的平方
        
if __name__ == '__main__':
    main()