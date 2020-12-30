#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:43:08 2019

@author: xie
"""
n = int(input())
ls = list(map(int, input().split()))
avg = 0
for p in ls:
    avg += p
avg = avg//n

ans = 0
def make(i):
    global ans
    global avg
    global ls
    if ls[i] != avg:
        ans += 1
        ls[i+1] += ls[i]-avg
        ls[i] = avg
    if i != n-2:
        return make(i+1)
    elif i == n-2:
        if ls[-1] != avg:
            ans += 1

make(0)
print(ans)