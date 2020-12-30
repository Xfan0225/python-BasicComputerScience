#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:51:04 2019

@author: xie
"""
n, m = map(int, input().split())
ls = list(map(int, input().split()))
for t in range(m):
    i, j = map(int, input().split())
    ls[i-1], ls[j-1] = ls[j-1], ls[i-1]
ans = ''
for l in ls:
    print(l, end=' ')
