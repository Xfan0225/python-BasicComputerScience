#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:25:28 2019

@author: xie
"""

ls = []
n = int(input())
ansls = []
flag = 0
l = input()
i = 1

for t in l:
    if t == 'C':
        if len(ls) == 0:
            print('No')
            flag = 1
            break
        else:
            ansls.append(ls.pop(-1))
    elif t == 'B':
        ls.append(i)
        i += 1

    elif t == 'A':
        ansls.append(i)
        i += 1

if flag == 0:
    print('Yes')
    for c in ansls:
        print(c)
