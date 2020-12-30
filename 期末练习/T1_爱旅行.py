#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:38:14 2019

@author: xie
"""

n = int(input())
ls = []
ans = []
for i in range(n):
    a = list(map(int, input().split()))
    ls.append(a)

for i in range(n):
    for j in range(i+1, n):
        lenth = abs(ls[i][0]-ls[j][0])+abs(ls[i][1]-ls[j][1])
        ans.append(lenth)

print(min(ans))