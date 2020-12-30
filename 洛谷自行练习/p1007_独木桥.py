#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:31:10 2019

@author: xie
"""
l = int(input())
n = int(input())
ls = list(map(int, input().split()))
maxium = max(l+1-min(ls), max(ls)+1)
ls1 = []
for i in ls:
    ls1.append(abs((l+1)//2-i))
minium = min(ls1)
print((l+1)//2-minium, end=' ')
print(maxium)
