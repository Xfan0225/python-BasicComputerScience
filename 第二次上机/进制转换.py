#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:13:41 2019

@author: xie
"""

x = int(input())
y = int(input())
if x == y:
    print(0)
    print(1)

else:
    while x > y:
        mod = x % y 
        x = x // y
        print(mod)
        if x == y:
            print(0)
            print(1)
            break
    else:
        print(x)
