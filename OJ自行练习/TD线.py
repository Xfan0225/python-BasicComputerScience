#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:04:54 2019

@author: xie
"""
import math
N = int(input())
x = 0
for i in range(N):
    x = x + int(input())
if N < 15:
    time = (48-x)/(15-N)
    time = math.ceil(time)
    if time <= 10:
        print(time)
    elif time > 10:
        print('gg')
elif N == 15:
    if x < 48:
        print('gg')
    elif x >= 48:
        print('0')