#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 11:05:09 2019

@author: Robin.J

E-mail: jrb1451144759@gmail.com

To: Life is short, I am learning python.
"""
import sys,time
for i in range(100):
    k = i + 1
    str = '#'*(i//2)+' '*((100-k)//2)
    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
    sys.stdout.flush()
    time.sleep(0.1)
