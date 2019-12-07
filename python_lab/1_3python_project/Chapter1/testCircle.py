#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:51:56 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

class Circle1:  #私有化方法
    def __init__(self, radius):
        self.__radius = radius #__radius实际上是一个私有数据，不应该被直接使用
    def setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else: raise ValueError("Value must be positive")
    def area(self):
        return 3.14159 * (self.__radius ** 2)

class Circle2:  #属性定义特性创建了一个只写特性radius，只读特性area方法
    def __init__(self, radius):
        self.__radius = radius
    
    def __setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else: raise ValueError("Value must be positive")
    radius = property(None, __setRadius)
    
    @property
    
    def area(self):
        return 3.14159 * (self.__radius ** 2)