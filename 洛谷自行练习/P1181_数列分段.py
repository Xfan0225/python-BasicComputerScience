#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:54:16 2019

@author: xie
"""

n, m = map(int, input().split())
ls = list(map(int, input().split()))
temp = 0
ans = 0
for i in ls:
    if i+temp > m:
        temp = i
        ans += 1
    elif i+temp <= m:
        temp += i
if temp != m:
    ans += 1
print(ans)
