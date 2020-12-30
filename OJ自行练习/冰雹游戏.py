#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:58:00 2019

@author: xie
"""

x =int(input())
if x == 1:
    print('1')
while x != 1:
    while x %2 == 1:
        x = 3*x +1
        print(int(x))
        
    while x %2 == 0:
        x = x/2
        print(int(x))
        
    