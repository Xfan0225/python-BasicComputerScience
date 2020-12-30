#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:11:29 2019

@author: xie
"""

num = int(input())
ls = [5, 4, 3, 2, 1]
a = 1
while a % num != 0:
    a = ls.pop(-1)
    i = int(str(a)[-1])
    if a*10 < 10000000:
        if i == 1:
            ls.append(a*10+5)
            ls.append(a*10+3)
        elif i == 2:
            ls.append(a*10+4)
            ls.append(a*10+3)
        elif i == 3:
            ls.append(a*10+4)
            ls.append(a*10+1)
        elif i == 4:
            ls.append(a*10+5)
        elif i == 5:
            ls.append(a*10+5)
            ls.append(a*10+4)
            ls.append(a*10+3)
            ls.append(a*10+2)
            ls.append(a*10+1)
else:
    print(a)
