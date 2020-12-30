#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:03:11 2019

@author: xie
"""

n = int(input())
cal = 0
time = 0
flag = 0
while True:
    cal += 1
    for i in range(1,cal+1):
        time += 1
        if time == n and cal % 2 == 0:
            print(str(i)+'/'+str(cal-i+1))
            flag = 1
            break
        elif time == n and cal % 2 == 1:
            print(str(cal-i+1)+'/'+str(i))
            flag = 1
            break
    if flag == 1:
        break
