#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:49:43 2019

@author: xie
"""
n = int(input())
m = int(input())
ls = []

for i in range(n):
    ls.append(i+1)

while len(ls) > 1:
    for i in range(m-1):
        ls.append(ls.pop(0))
    ls.pop(0)

print(ls[0])