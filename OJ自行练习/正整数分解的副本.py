#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:17:37 2019

@author: xie
"""

def split(n, m):
    if n == 0:
        return 1

    elif m == 0:
        return 0

    else:
        ans = split(n ,m-1)
        while n >= m:
            n -= m
            ans += split(n, m-1)
        return ans

t = int(input())

print(split(t, t))


'''
def make(n, m):
    if n == 0:
        return 1
    elif m == 0:
        return 0
    else:
        res = make(n, m - 1)
        while n >= m:
            n -= m
            res += make(n, m - 1)
        return res

n = int(input())

print(make(n, n))
'''