#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:06:00 2019

@author: xie
"""

n, m = map(int, input().split())
ls = []
ans = 0
for i in range(n):
    t = ((m+n)/n)*i
    if t % 1 <= 0.5:
        ans += t%1
    elif t % 1 > 0.5:
        ans += 1-t%1

print(ans)
