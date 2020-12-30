#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:08:29 2019

@author: xie
"""

n = input().split('-')
ans0 = ''
ans = 0

for i in n[:-1]:
    ans0 += str(i)

t = 1

for c in ans0:
    ans += int(c)*t
    t += 1

if n[-1] == 'X':
    if ans % 11 == 10:
        print('Right')
    else:
        for i in n[:-1]:
            print(i, end='-')
        print(ans % 11)
else:
    if ans % 11 == int(n[-1]):
        print('Right')
    else:
        for i in n[:-1]:
            print(i, end='-')
        print(ans % 11 if ans%11 != 10 else 'X')

