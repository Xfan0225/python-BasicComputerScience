#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:58:53 2019

@author: xie
质数筛法
"""

a,b = map(int,input().split())
ls = []
ans = 0

for i in range (2,b):
    ls.append(i)



'''
for m in range(50):
    for t in ls[m:]:
        if t % ls[m-1] == 0 and t/ ls[m-1] != 1:
            ls.remove(t)
'''

for z in ls:
    if z >= a:
        ans += z
    elif z > b:
        break
    else:
        continue

print(ans)