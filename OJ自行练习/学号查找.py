#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:20:27 2019

@author: xie
"""

n = int(input())
d = {}
for i in range (n):
    numb = str(input())
    name = str(input())
    d[numb]=name
ls = []
k= int(input())
for t in range (k):
    s = str(input())
    if s in d:
        ls.append(d.get(s))
    else:
        ls.append('Not Found!')
        
for x in ls:
    print(x)