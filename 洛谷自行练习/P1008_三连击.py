#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:34:29 2019

@author: xie
"""

for i in range(100, 333):
    ls_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = str(i*2)
    b = str(i*3)
    ls = []
    for t in a:
        ls.append(t)
    for s in str(i):
        ls.append(s)
    for c in b:
        ls.append(c)
    for x in ls:
        if int(x) in ls_a:
            ls_a.remove(int(x))
    if len(ls_a) == 0:
        print(i, end=' ')
        print(a, end=' ')
        print(b)
