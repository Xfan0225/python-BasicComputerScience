#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:46:52 2019

@author: xie
"""
i = 1
x = 0
k = int(input())
while x <= k:
    x += 1/i
    i += 1
else:
    print(i-1)
