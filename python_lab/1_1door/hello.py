#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 15:31:50 2019

@author: apple
"""
#1.input输入例子
temp = input("请输入：")
#helloguess = int(temp)
if temp == 'hello':
    print("ok")
else:
    print("error")
print("game end!")

#2.while例子

count = 0
while (count < 9):
    print('The count is:', count)
    count = count + 1
print("good bye!")