#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:58:45 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""
"""
题目2：设计一个函数，生成指定长度的验证码（由数字和大小写英文字母构成的随机字符串）
"""
from random import randint

def generate_code(length = 4):
    """
    :param length:验证码长度
    :return:返回一个指定长度的有效数字，字母组成的验证码
    """
    code_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = ''
    for _ in range(length):
        code += code_string[randint(0, len(code_string) - 1)]
    return code

def main():
    for _ in range(10):
        print(generate_code())
        
if __name__ == '__main__':
    main()