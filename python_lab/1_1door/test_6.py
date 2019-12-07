#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:35:42 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

题目6: 设计一个函数，对传入的字符串（假设字符串中只包含小写字母和空格）进行加密操作，
加密的规则是a变d，b变e，c变f，……，x变a，y变b，z变c，空格不变，返回加密后的字符串

"""

def caesar_encrypt(string):
    """
    :param string:给定一个字符串
    :return:返回加密后的字符串
    
    """
    new_string = ''
    all_string = 'abcdefghijklmnopqrstuvwxyz'
    for x in string:
        if x in all_string:
            index = all_string.find(x)
            if index >= len(all_string) - 3:
                new_string += all_string[len(all_string) - index + 3]
            else:
                new_string += all_string[index + 3]
            print(new_string)
        else:
            new_string += x
    return new_string

def main():
    print(caesar_encrypt('attack at dawn'))
    print(caesar_encrypt('dinner is on me'))
    string_input = input()
    print(caesar_encrypt(string_input))
    
if __name__ == '__main__':
    main()