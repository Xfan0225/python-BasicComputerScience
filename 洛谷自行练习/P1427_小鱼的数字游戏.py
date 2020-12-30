#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:59:08 2019

@author: xie
"""

ls = input().split()
t = len(ls)
for i in range(2, t+1):
    print(ls[t-i], end=' ')
