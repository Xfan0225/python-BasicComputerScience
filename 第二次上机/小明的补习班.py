#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:07:22 2019

@author: xie
"""

good = int(input())
low = int(input())
if abs(good-low) <= 10:
    print('2000')
elif good-low > 10:
    money = 2000+15*(good-10)-10*low
    if money <= 3000:
        print(money)
    else:
        print('3000')
elif low-good >10:
    money = 2000+15*good-20*(low-10)
    if money >= 1000:
        print(money)
    else:
        print('1000')