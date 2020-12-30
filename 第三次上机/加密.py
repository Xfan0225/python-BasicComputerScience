#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:01:13 2019

@author: xie
"""
dict1 = {}
ls1 = list(map(str, input().split()))
ls2 = list(map(str, input().split()))

for i in range(len(ls1)):
    dict1[ls1[i]] = ls2[i]

for x in str(input()):
     print(dict1.get(x), end='')
