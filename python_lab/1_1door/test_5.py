#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:07:54 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

"""

设计一个函数，判断传入的整数列表（要求元素的个数大于2个）中的元素能否构成等差数列

"""

def is_arithmetic_series(num_list):
    """
    
    :param num_list:给定需要判断的列表
    :return:是等差数列返回True,否则返回False
    
    """
    num_list_len = len(num_list)
    assert num_list_len > 2
    sorted_list = sorted(num_list)
    #print(sorted_list)
    for index in range(2, num_list_len):
        if sorted_list[index] - sorted_list[index - 1] != \
        sorted_list[index - 1] - sorted_list[index - 2]:
            return False
    return True

def main():
    list1 = [1, 3, 5, 7, 9]
    list2 = [100, 500, 200, 400, 300]
    list3 = [1, 2, 3, 4, 5, 7]
    print(is_arithmetic_series(list1))
    print(is_arithmetic_series(list2))
    print(is_arithmetic_series(list3))
    
if __name__ == '__main__':
    main()