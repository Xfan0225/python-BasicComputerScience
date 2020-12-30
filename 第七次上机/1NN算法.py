#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:16:29 2019

@author: xie
"""

import numpy as np
n = int(input())
ls = []
for i in range(n):
    ls.append(list(map(int, input().split())))

kind = list(map(int, input().split()))
inp = list(map(int, input().split()))
ans = 0
ansls = []
for i in ls:
    cal = list((np.array(inp)-np.array(i))**2)
    for p in cal:
        ans += p
    ansls.append(ans)
    ans = 0
print(kind[ansls.index(min(ansls))])
