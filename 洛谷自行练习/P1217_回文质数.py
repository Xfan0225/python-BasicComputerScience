#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:10:24 2019

@author: xie
"""

a, b = map(int, input().split())
ls = []
for i in range(a,b):
    if str(i)[::-1] == str(i):
        if i % 2 != 0 and i % 3 != 0 and i % :
            ls.append(i)

for i in ls:
    for t in range(5, i//2 , 2):
        if i % t == 0 and i != t:
            ls.remove(i)
            break

for i in ls:
    print(i)

