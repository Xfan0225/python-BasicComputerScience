#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:55:46 2019

@author: xie
"""
import math
n, m = map(int, input().split())
dic = {}
for i in range(n):
    k, s = map(int, input().split())
    dic[k] = s
ls = list(dic.items())
ls.sort(key=lambda x:x[1])
people = math.floor(m*1.5)
score = ls[-people][1]

for i in range(-people-1, -n-1, -1):
    if ls[i][1] == score:
        people += 1
    else:
        break

print(score,end=' ')
print(people)
for i in range(people):
    print(ls[n-i-1][0],end=' ')
    print(ls[n-i-1][1])
