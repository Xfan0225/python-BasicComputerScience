#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 21:23:55 2019

@author: xie
"""

n, m = map(int, input().split())
ls = []
ansls = []
s = 0
t = 0
if m != n:
    m = m % n
for i in range(n):
    ls.append(True)

while len(ansls) < n:
    if t >= n:
        t = 0

    if ls[t]:
        s += 1
        if s == m:
            ansls.append(t+1)
            ls[t] = False
            s = 0
            t += 1
        else:
            t += 1
    else:
        t += 1

for ans in ansls:
    print(ans, end=' ')
