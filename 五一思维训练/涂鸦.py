#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:17:17 2019

@author: xie
"""

n, m, k = map(int, input().split())
ls = []
for i in range(n):
    ls.append([])
    for t in range(m):
        ls[i].append(0)

for i in range(k):
    op, num, col = map(int, input().split())
    if op == 1:
        for i in range(m):
            ls[num-1][i] = col
    elif op == 2:
        for i in range(n):
            ls[i][num-1] = col

for i in range(n):
    for t in range(m-1):
        print(ls[i][t],end = ' ')
    print(ls[i][m-1])


