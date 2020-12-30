#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:03:43 2019

@author: xie
"""

dict1 = {'0001': 'A', '0010': 'B', '0011': 'C', '0000': 'D', '0100': 'E', '1111': 'F', '0101': 'G', '1001': 'H'}
x = input()
ls = []
ans = ''
s = 0

for i in range(int(len(x)/4)):
    ls.append(x[4*i:4*(i+1)])

for t in ls:
    if t not in dict1:
        print('Not Found!')
        s = 1
        break
    else:
        ans += dict1.get(t)
     
if s == 0:
    print(ans)
