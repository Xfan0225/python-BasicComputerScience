#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:39:58 2019

@author: xie
"""

dic = {}
val = []
m, n, k = map(int, input().split())
for i in range(m):
    ls = list(map(int, input().split()))
    val.append(ls)
    for j in range(n):
        if ls[j] != 0:
            dic[ls[j]] = (i,j)

ls = sorted(list(dic.keys()),reverse = True)

k -= dic[ls[0]][0]+2
i = 0
ans = 0
for t in ls:
    if i == len(ls)-1:
        ans += ls[-1]
        break
    if k >= abs(dic[ls[i]][0]-dic[ls[i+1]][0])+abs(dic[ls[i]][1]-dic[ls[i+1]][1])+dic[ls[i+1]][0]+2:
        x = dic[t][0]
        y = dic[t][1]
        ans += val[x][y]
        k -= abs(dic[ls[i]][0]-dic[ls[i+1]][0])+abs(dic[ls[i]][1]-dic[ls[i+1]][1])+1
        i += 1
    else:
        ans += t
        break

if k < 0:
    ans = 0
print(ans)
