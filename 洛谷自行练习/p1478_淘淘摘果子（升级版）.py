#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:28:21 2019

@author: xie
"""

n, s = map(int, input().split())
a, b = map(int, input().split())
ls = []
ans = 0

for i in range(n):
    xi, yi = map(int, input().split())
    if xi <= a+b:
        ls.append(yi)

ls.sort()

for i in ls:
    if s - i >= 0:
        s -= i
        ans += 1
    else:
        break

print(ans)