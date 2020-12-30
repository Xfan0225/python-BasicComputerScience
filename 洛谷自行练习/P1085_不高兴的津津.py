#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:47:35 2019

@author: xie
"""
ls = []
for i in range(7):
    m, n = map(int, input().split())
    ls.append(m+n)
a = max(ls)
if a <= 8:
    print(0)
else:
    print(ls.index(a)+1)
