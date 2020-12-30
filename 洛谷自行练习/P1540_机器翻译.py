#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:18:10 2019

@author: xie
"""

m, n = map(int, (input().split()))
ls = []
time = 0
t = 1
inp = input().split()
for word in inp:
    if word not in ls and len(ls) < m:
        ls.append(word)
        time += 1
    elif word in ls:
        continue
    elif word not in ls and len(ls) >= m:
        if t % m != 0:
            ls[t % m - 1] = word
            time += 1
            t += 1
        elif t % m == 0:
            ls[-1] = word
            time += 1
            t += 1
print(time)
