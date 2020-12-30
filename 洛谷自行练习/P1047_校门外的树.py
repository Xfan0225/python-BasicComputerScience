#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:51:12 2019

@author: xie
"""

l, m = map(int, input().split())
ls = []

for i in range(l+1):
    ls.append(True)

for t in range(m):
    p, q = map(int, input().split())
    for s in range(p, q+1):
        ls[s] = False

for x in ls:
    if x:
        ans += 1

print(ans)
