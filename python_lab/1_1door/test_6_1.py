#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:58:46 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

题目6: 设计一个函数，对传入的字符串（假设字符串中只包含小写字母和空格）进行加密操作，
加密的规则是a变d，b变e，c变f，……，x变a，y变b，z变c，空格不变，返回加密后的字符串

"""

def caesar_encrypt(string):
    base = ord('a')
    encrypted_string = ''
    for ch in string:
        if ch != ' ':
            curr = ord(ch)
            diff = (curr - base + 3) % 26
            ch = chr(base + diff)
        else:
            encrypted_string += ' '
        encrypted_string += ch
    return encrypted_string


def main():
    print(caesar_encrypt('attack at dawn'))
    print(caesar_encrypt('dinner is on me'))

if __name__ == '__main__':
    main()


    