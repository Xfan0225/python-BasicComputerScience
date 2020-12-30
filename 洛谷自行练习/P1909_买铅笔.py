#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 00:12:03 2019

@author: xie
"""

ls = []
t = int(input())
for i in range(3):
    m, n = map(int, input().split())
    if t % m != 0:
        time = t // m + 1
    elif t % m == 0:
        time = t // m
    money = time*n
    ls.append(money)

print(min(ls))
