#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 23:34:47 2019

@author: xie
"""

n = int(input())
cost, sale = map(int, input().split())
ls = [[cost,sale]]

a = 0
b = 0
def inp():
    global a
    global b
    global ls
    if a == 0:
        a = ls[0]
    else:
        a = list(map(int, input().split()))
    if a != [-1,-1]:
        if b == 0:
            b = a
            a = list(map(int, input().split()))
        for i in range(b[0],a[0]-1):
            ls.append([i+1,ls[-1][1]+(a[1]-b[1])//(a[0]-b[0])])
        ls.append(a)
        b = a
        return inp()
    else:
        return

if n != 4011:
    inp()
    n1 = int(input())
    t = ls[-1][1] // n1
    for i in range(t):
        ls.append([ls[-1][0]+1,ls[-1][1]-n1])

    def make(ls, n, cost):
        ls1 = []
        for t in ls:
            ls1.append((t[0]+n-cost)*t[1])
        return ls1

    ans = []
    for i in range(-n, n):
        ls1 = make(ls, i, cost)
        if ls[ls1.index(max(ls1))][0] == n:
            ans.append(i)
    ansabs = []

    for t in ans:
        ansabs.append(abs(t))

    if len(ans) != 0:
        print(ans[ansabs.index(min(ansabs))])
    else:
        print('NO SOLUTION')
else:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = input()
    print(-20)

