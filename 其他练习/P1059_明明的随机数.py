#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:50:43 2019

@author: xie
"""
n = int(input())
ls = list(map(int, input().split()))
ls = sorted(list(set(ls)))
print(len(ls))
for i in ls:
    print(i, end=' ')
