#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:13:21 2019

@author: xie
"""

def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb(n-1)+climb(n-2)

print(climb(int(input())))
