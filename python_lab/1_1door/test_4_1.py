#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:50:20 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

设计一个函数，统计字符串中英文字母和数字各自出现的次数

"""

def count_letter_number(string):
    letter_count = 0
    digit_count = 0
    for ch in string:
        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            letter_count += 1
        elif '0' <= ch <= '9':
            digit_count += 1
    return letter_count, digit_count


def main():
    print(count_letter_number('asdkj31107098qwlerjFALJSDFA'))
    print(count_letter_number('23452345werwhwhwwertww'))
    print(count_letter_number('sdfg314351SSFHGKHGLK@786587'))
    
if __name__ == '__main__':
    main()