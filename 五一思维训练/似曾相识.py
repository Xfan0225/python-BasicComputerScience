#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 01:34:27 2019

@author: xie
"""

n, m = map(int, input().split())
dic = {}

for i in range(n):
    p = tuple(input().split())
    if dic.get(p, True):
        print('YES')
        dic[p] = False
    else:
        print('NO')
