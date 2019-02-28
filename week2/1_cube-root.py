#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python 3.0
Created on Fri Feb 22 23:35:00 2019

@author: geyuanjun
"""

x = int(input('Enter a number: '))
for ans in range(0, abs(x + 1)):
    if ans ** 3  >= abs(x):
        break
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))