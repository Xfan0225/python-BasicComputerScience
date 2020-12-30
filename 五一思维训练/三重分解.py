#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 01:21:59 2019

@author: xie
"""

n = int(input())
if n < 3:
    print('impossible!')
elif n % 3 == 0:
    print('YES')
    print(1, 1, n-2)
elif n % 3 == 1:
    print('YES')
    print(1, 2, n-3)
elif n % 3 == 2:
    print('YES')
    print(2, 2, n-4)
