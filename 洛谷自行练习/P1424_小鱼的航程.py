#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:53:39 2019

@author: xie
"""

x, n = map(int, input().split())
ans = 0
t = 1
while t <= n:
    if x % 7 != 0 and x % 7 != 6:
        ans += 250
        x += 1
        t += 1
    else:
        x += 1
        t += 1
print(ans)
