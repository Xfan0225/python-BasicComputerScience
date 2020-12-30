#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:09:57 2019

@author: xie
"""

def make(a, b):
    if a%b == 0:
        return b
    else:
        m = b
        n = a%b
        return make(m, n)

n = int(input())
ls = list(map(int, input().split()))
a = ls[0]
ans = ls[1]-ls[0]
for i in range(n-2):
    if ans % (ls[i+2]-ls[i+1]) == 0:
        ans = ls[i+2]-ls[i+1]

    elif ans > (ls[i+2]-ls[i+1]) and ans % (ls[i+2]-ls[i+1]) != 0:
        ans = make(ls[i+2]-ls[i+1], ans)
    elif ans < (ls[i+2]-ls[i+1]) and (ls[i+2]-ls[i+1]) % ans != 0:
        ans = make(ls[i+2]-ls[i+1], ans)
    if ans == 1:
        break

print(a, end=' ')
print(ans)
