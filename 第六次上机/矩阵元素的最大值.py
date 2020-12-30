#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:50:50 2019

@author: xie
"""

n = int(input())
ls = []
for i in range(1, n+1):
    if i % 2 == 1:
        ls.append([1])
    elif i % 2 == 0:
        ls.append([2])
    for j in range(1, n+1):
        if i == 1 and j % 2 and j != 1:
            ls[0].append(1)
        elif i == 1 and j % 2 == 0:
            ls[0].append(2)
        elif j != 1:
            ls[i-1].append(0)

for i in range(1,n):
    for j in range(1,n):
        ls[i][j] = ls[i-1][j]+ls[i][j-1]

print(ls[-1][-1])