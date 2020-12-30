#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:17:20 2019

@author: xie
"""

import math
n = int(input())
ls = []
a = 2
b = 20000
f = min(a, b)
t = math.sqrt(b + 0.5) #t是sqrt(b)的值
i = 2
p = [True] * (b + 5) #用一个True/False列表表示是否是质数，一开始都是True。这样筛的过程就只需要把True变成False 比较高效
p[1] = False
while i <= t:
   if p[i]: #找到质数啦，开筛~
       j = i * i #小小的优化，大家可以思考一下为什么可以从j开始筛呢？？
       while j <= b:
           p[j] = False
           j += i#筛掉一个又一个……
   i += 1
i = a
ans = 0

while i <= b:  #这里开始，我们统计一下质数的和~
   if p[i]:
       ls.append(i)
   i += 1
flag = 0

for i in ls:
    for t in ls:
        if n-t-i in ls:
            print(i, end=' ')
            print(t, end=' ')
            print(n-t-i)
            flag = 1
            break
    if flag == 1:
        break