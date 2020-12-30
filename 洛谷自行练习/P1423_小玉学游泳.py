#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:50:43 2019

@author: xie
"""

ans = 2
n = 1
lenth = float(input())
while ans < lenth:
    ans += 2*0.98**n
    n += 1
else:
    print(n)
