#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:30:19 2019

@author: xie
"""

n, m = map(int, input().split())
ls = []
for i in range(m):
    ls.append([])
for i in range(m):
    ls[i] = list(map(int, input().split()))
ls.sort()
ans = 0
count = 0
for i in range(m):
    temp = ls[i][-1]
    if temp + count >= n:
        ans += ls[i][0]*(n-count)
        break
    else:
        ans += ls[i][0]*temp
        count += temp
print(ans)
