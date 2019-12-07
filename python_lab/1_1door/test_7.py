#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 22:41:00 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

题目8: 设计一个函数，统计一个字符串中出现频率最高的字符及其出现次数

"""

def find_most_freq(string):
    """
    :param string:输入一个字符串
    :return:返回字符串中出现频率最高的字符及其出现的次数
    """
    my_dict = {}
    for x in string:
        if x not in my_dict:
            my_dict[x] = 1
        else:
            my_dict[x] += 1
    max_num = 0
    for y in my_dict:
        if my_dict[y] > max_num:
            max_num = my_dict[y]
    max_list = []
    for z in my_dict:
        if my_dict[z] == max_num:
            max_list += z
    return max_list, max_num

def main():
    print(find_most_freq('aabbaaccddbb'))
    print(find_most_freq('hello, world!'))
    print(find_most_freq('asd13adsf13412'))
    
if __name__ == '__main__':
    main()