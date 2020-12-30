#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 00:35:25 2019

@author: xie
"""

n = int(input())
ls = list(map(int, input().split()))
ansls = []
for t in range(n):
    ansls.append(0)
for i in range(0,n,-1):
    a = ls[i]
    if i+1 < n:
        b = ls[i+1]
    if i+2 < n:
        c = ls[i+2]
    if i == n-1:
        ansls[i] = min(a, 20)
    elif i == n-2:
        ansls[i] = min(a+b , 30, 20+a, 20+b)
    elif i == n-3:
        ansls[i] = min(a+b+c, a+30, c+30, 40, a+b+20, a+c+20, b+c+20)
    else:
        ansls[i] = min(ls[i]+ansls[i+1],20+ansls[i+1],30+ansls[i+2],40+ansls[i+3])

print(ansls[0])