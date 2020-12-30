#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 12:54:59 2019

@author: xie
"""

n, m = map(int, input().split())            #n为菜品数，m为钱数
ls1 = list(map(int, input().split()))
def fuck(ls1,n,m):
    ls = []
    for i in range(n):
        ls.append([])
        for j in range(m):
            ls[i].append(0)

    for i in range(n):
        for j in range(m):
