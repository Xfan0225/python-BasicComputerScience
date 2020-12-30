#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:02:10 2019

@author: xie
"""

a = int(input())
b= int(input())

def get(a, b):

    if a%b == 0:
        return b
    else:
        m = b
        n = a%b
        return get(m, n)

if b >= 400760000000:
    print('impossible!')
else:
    ans = int(a*b/get(a, b))
    if ans >= 400760000000:
        print('impossible!')
    else:
        print(ans)
