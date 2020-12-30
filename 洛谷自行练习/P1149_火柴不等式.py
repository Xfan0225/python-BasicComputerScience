#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:13:00 2019

@author: xie
"""

n = int(input()) - 4
dic = {'0':6, '1':2, '2':5, '3':5,'4':4, '5':5,'6':6,'7':3,'8':7,'9':6}
def make(a,b,c,n):
    cal = 0
    for i in str(a):
        cal += dic[i]
    for i in str(b):
        cal += dic[i]
    for i in str(c):
        cal += dic[i]
    if cal == n:
        return 1
    else:
        return 0

ans = 0
a = 0
b = 0
c = 0
for x in range (750):
    a = x
    for y in range(750):
        b = y
        c = x + y
        ans += make(a,b,c,n)
print(ans)