#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:23:11 2019

@author: xie
"""

def func(a, b, c):
    dic = {}
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return func(20, 20, 20)
    #elif a == b and b == c:
        #return 2**a
    #elif a==b and b == c-1:
        #return 2**a
    #elif a == b and b == c or b == c-1:
        #return 2**a
    elif a<b and b<c:
        if (a, b, c) in dic:
            return dic[(a, b, c)]
        else:
            ans = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
            dic[(a, b, c)] = ans
            return ans
    else:
        if (a, b, c) in dic:
            return dic[(a, b, c)]
        else:
            ans = func(a-1, b ,c) + func(a-1, b-1, c)+ func(a-1, b, c-1) - func(a-1, b-1, c-1)
            dic[(a, b, c)] = ans
            return ans

a, b, c = 0, 0, 0

lsa = []
lsb = []
lsc = []
n = 0
while True:
    if a == b and b == c and a == -1:
        break
    a, b, c = map(int, input().split())
    lsa.append(a)
    lsb.append(b)
    lsc.append(c)
    n += 1

for i in range(n-1):
    print('w('+str(lsa[i])+', '+str(lsb[i])+', '+str(lsc[i])+') = '+str(func(lsa[i], lsb[i], lsc[i])))

