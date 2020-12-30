#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:53:38 2019

@author: xie
"""

n, m = map(int, input().split())   #n重量（总钱数），m物品个数
lsv = []        #价格（重量）
lsp = []        #重要度（价格）

for i in range(m):
    v, p = map(int, input().split())
    lsv.append(v)
    lsp.append(p)

def fuck(lsv,lsp,m,n):
    load = []
    for i in range(m):
        load.append([])
        for t in range(n):
            load[i].append(0)

    #load[i][j]代表前i个物品装入承重j的背包的总价值,行表示装了几个东西，列表示价格
    for i in range(m):              #装入的第i个物品
        for j in range(n):          #装入的价值
            load[i][j] = load[i-1][j]
            if j >= lsv[i] and load[i-1][j-lsv[i]] + lsp[i]*lsv[i] > load[i-1][j]:
                load[i][j] = load[i-1][j-lsv[i]]+lsp[i]*lsv[i]

    return load[m-1][n-1]

print(fuck(lsv,lsp,m,n))



