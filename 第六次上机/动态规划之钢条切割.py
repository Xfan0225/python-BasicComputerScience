#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:18:14 2019

@author: xie
"""

n = int(input())                            #n代表收益
price = list(map(int, input().split()))
m = int(input())                            #m代表长度
lenth = list(map(int, input().split()))

value = []

for i in range(max(lenth)+1):
    if i == 0:
        value.append(0)
    elif i == 1:
        value.append(price[0])
    else:
        if i <= n:
            value.append(price[i-1])
        else:
            value.append(0)
        for j in range(1,i):
            if value[j]+value[i-j] > value[i]:
                value[i] = value[j]+value[i-j]

for t in lenth:
    print(value[t])



