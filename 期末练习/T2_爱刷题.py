#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:44:14 2019

@author: xie
"""

n = int(input())
ls = []
ans = []
for i in range(n):
    k, s = input().split()
    if int(k) == 0:
       ls.append([int(k),s])
    elif int(k) == 1:
        if [0, s] not in ls:
            ans.append('NO')
        else:
            loc = ls.index([0,s])
            ans.append(loc+1)
            for i in range(loc+1):
                ls.pop(0)

for i in ans:
    print(i)