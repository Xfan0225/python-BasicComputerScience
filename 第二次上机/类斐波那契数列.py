#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 13:53:23 2019

@author: xie
"""
x1 = int(input())
x2 = int(input())
n = int(input())
for i in range(n-1):
    x1 = x1*x2
    x1,x2 = x2,x1
  
print(x1)
