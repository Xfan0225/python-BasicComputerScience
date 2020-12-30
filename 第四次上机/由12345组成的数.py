#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:48:56 2019

@author: xie
"""

num = int(input())
ls = [1,2,3,4,5]

while ls[0] % num != 0:
    i = int(str(ls[0])[-1])
    if i == 1:
        ls.append(ls[0]*10+3)
        ls.append(ls[0]*10+5)
    elif i == 2:
        ls.append(ls[0]*10+3)
        ls.append(ls[0]*10+4)
    elif i == 3:
        ls.append(ls[0]*10+1)
        ls.append(ls[0]*10+4)
    elif i == 4:
        ls.append(ls[0]*10+5)
    elif i == 5:
        ls.append(ls[0]*10+1)
        ls.append(ls[0]*10+2)
        ls.append(ls[0]*10+3)
        ls.append(ls[0]*10+4)
        ls.append(ls[0]*10+5)
    ls.pop(0)
else:
    print(ls[0])