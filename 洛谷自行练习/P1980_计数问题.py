#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:59:02 2019

@author: xie
"""

ans = 0
n, x = map(int, input().split())

for i in range(1, n+1):
    ans += str(i).count(str(x))

print(ans)
