#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:49:13 2019

@author: xie
"""
gpals = []
N = int(input())
for i in range (N):
    x = int(input())
    if x < 60:
        gpa = 0
        gpals.append(gpa)
    elif x == 60:
        gpa = 1
        gpals.append(gpa)
    else:
        gpa = 4 - 3*(100-x)**2/1600
        gpals.append(gpa)

s = 0
avg = 0

for t in range (N):
    y = float(input())
    s += y
    avg = avg + y * gpals[t]
    
    
print('{:.3f}'.format(avg/s))