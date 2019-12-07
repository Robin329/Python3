#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 21:57:24 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""

while True:
    command = input('Enter a command[rwq]:')
    if 'q' in command.lower():break
    if command.lower() == 'r':
        print('process \'r\'')
    elif command.lower() == 'w':
        print('process \'w\'')
    else:
        print('Invalid command, try again')