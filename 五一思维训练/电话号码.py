#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:50:07 2019

@author: xie
"""

n = int(input())
ls = list(map(int, input().split()))
time = (n-8)//2
count = 0
for i in range(n-8+1):
    if ls[i] == 8:
        count += 1
if count > time:
    print('YES')
else:
    print('NO')
