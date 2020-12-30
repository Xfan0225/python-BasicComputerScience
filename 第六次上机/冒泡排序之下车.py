#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:09:24 2019

@author: xie
"""

m = int(input())
ls = list(map(int, input().split()))
ans = 0
for i in range(m-1):
    for j in range(m-i-1):
        if ls[j] > ls[j+1]:
            ls[j], ls[j+1] = ls[j+1], ls[j]
            ans += 1
            flag = False
print(ans)