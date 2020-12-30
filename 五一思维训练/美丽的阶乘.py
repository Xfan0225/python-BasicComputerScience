#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 01:18:11 2019

@author: xie
"""

n = int(input())
ans = 0
while n // 5 > 1:
    ans += n // 5
    n = n // 5
else:
    if n >= 5:
        ans += 1

print(ans)