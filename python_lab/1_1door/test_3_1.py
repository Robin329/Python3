#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:32:44 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""
题目2：设计一个函数，生成指定长度的验证码（由数字和大小写英文字母构成的随机字符串）
"""

from random import randrange

def generate_code(length = 4):
    all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    all_chars_len = len(all_chars)
    code = ''
    for _ in range(length):
        index = randrange(all_chars_len)
        #print(index)
        code +=all_chars[index]
    return code

def main():
    for _ in range(5):
        print(generate_code())

if __name__ == '__main__':
    main()