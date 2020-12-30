#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:13:06 2019

@author: xie
"""

s, x = map(int, input().split())
flag = 0
lenth = 0
i = 0
while flag == 0:
    if lenth >= s-x:
        if lenth + 7*(0.98**(i+1)) <= s+x:
            print('y')
            flag = 1
        else:
            print('n')
            flag = 1
    lenth += 7*(0.98**i)
    i += 1
