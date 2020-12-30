#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:51:03 2019

@author: xie
"""

a, b, c = map(int, input().split())
flag1 = 0
for i in range(1, 999):
    ls = []
    flag = 0
    for t in str(i*a):
        if i*a >= 100 and i*a <= 999 and t != '0':
            if t not in ls:
                ls.append(t)
            else:
                flag = 1
                break
        else:
            flag = 1

    for x in str(i*b):
        if i*b > 999 or flag == 1 or i*b < 100 or x == '0':
            flag = 1
            break
        else:
            if x not in ls:
                ls.append(x)
            else:
                flag = 1
                break

    for y in str(i*c):
        if i*c > 999 or flag == 1 or i*c < 100 or y == '0':
            flag = 1
            break
        else:
            if y not in ls:
                ls.append(y)
            else:
                flag = 1
                break
    if '0' in ls:
        flag == 1

    if flag == 0:
        flag1 = 1
        print(i*a, end=' ')
        print(i*b, end=' ')
        print(i*c)
if flag1 == 0:
    print('No!!!')