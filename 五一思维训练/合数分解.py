#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 19:35:24 2019

@author: xie
"""

n = int(input())
if n % 4 == 0:
    print(n//4)
elif n % 4 == 1:
    if n >= 9:
        print((n-9)//4 + 1)
    else:
        print(-1)
elif n % 4 == 2:
    if n >= 6:
        print((n-6)//4 + 1)
    else:
        print(-1)
elif n % 4 == 3:
    if n >= 15:
        print((n-15)//4 + 2)
    else:
        print(-1)
