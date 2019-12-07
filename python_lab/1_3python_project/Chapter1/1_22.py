#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:24:25 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

target = 66

while True:
    value = input('Enter an integer between 1 and 100')
    try:
        value = int(value)
        break
    except ValueError:
        print("I said enter an integer!")     
    if value > target:
        print(value, "is too high")
    elif int(value) < target:
        print("too low")
    else:
        print("Pefect")