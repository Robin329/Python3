#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:30:36 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""
设计一个函数，统计字符串中英文字母和数字各自出现的次数

"""
def count_letter_number(string):
    """
    :param string:Given a string
    :return:a tuple consisting of the number of occurrences of 
    English letters and numbers in a string
    
    """
    n = 0
    m = 0
    for s in string:
        if s in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            n +=1
        elif s in '0123456789':
            m +=1
    return n,m

def main():
    print(count_letter_number('as1234fasdf'))   #（7, 4）
    print(count_letter_number('qwerdas123411234'))  #(7, 9)
    print(count_letter_number('as1234142fafqwerqsdf'))  #(13, 7)
    
if __name__ == '__main__':
    main()