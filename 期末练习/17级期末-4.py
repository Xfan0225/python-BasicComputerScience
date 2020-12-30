#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:47:37 2019

@author: xie
"""
ans = 0
n, p = map(int, input().split())
for i in range(1,n+1):
    for t in str(i):
        if t == str(p):
            ans += 1
print(ans)