#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:47:17 2019

@author: xie
"""
n = int(input())
ls = [0,1]
for i in range(n-1):
    ls.append(ls[i]+ls[i+1])
for i in ls:
    print(i,end=' ')
