#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 00:13:13 2019

@author: xie
"""

n = int(input())
ls_raw = input().split()
ls = []

for t in ls_raw:
    ls.append(int(t))

n = 1

for i in ls:
    ans = 0
    for p in range(n):
        if ls[p] < i:
            ans += 1
    print(ans, end=' ')
    n += 1
