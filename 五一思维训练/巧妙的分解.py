#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 17:28:25 2019

@author: xie
"""
import math
n = int(input())
flag = 0
cal = 0
ansls = []
x = 0
su = 0
ls = []
for i in range(1,n+1):
    ls.append(i)
for i in range(1,(1+n)*n//2+1):
    if math.gcd(i, (1+n)*n//2) != 1:
        print('YES')
        flag = 1
        while i > n:
            cal += 1
            ansls.append(n-x)
            ls.remove(n-x)
            i -= n-x
            x += 1
        else:
            cal += 1
            ansls.append(i)
            ls.remove(i)
        print(cal, end=' ')
        for t in ansls[:-1]:
            print(t, end=' ')
        print(ansls[-1])
        print(n-cal, end=' ')
        for t in ls:
            print(t, end=' ')
        break

if flag == 0:
    print('impossible!')