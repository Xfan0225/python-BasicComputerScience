#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 20:00:49 2019

@author: xie
错因：可能存在多次变换后产生结果

"""

ans = []
t = int(input())
for i in range(t):
    q = int(input())
    ls0 = list(map(int, input().split()))   #计划
    ls1 = list(map(int, input().split()))   #规范
    ls00 = []
    ls10 = []
    if ls0[0] != ls1[0] or ls0[-1] != ls1[-1]:
        ans.append('NO')
    else:
        ls00 = [ ls0[i+1] - ls0[i] for i in range(q-1) ]
        ls10 = [ ls1[i+1] - ls1[i] for i in range(q-1) ]
        ls00.sort()
        ls10.sort()
        if ls00 == ls10:
            ans.append('YES')
        else:
            ans.append('NO')

for i in ans:
    print(i)


