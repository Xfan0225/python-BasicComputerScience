#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:52:01 2019

@author: xie
"""
x = int(input())
if x <= 150:
    x =x*0.4463
    print('{:.3f}'.format(x))
elif x <= 400:
    x = 150*0.4463 + (x-150)*0.4663
    print('{:.3f}'.format(x))
else:
    x = 150*0.4463 + 250*0.4663 + (x-400)*0.5663
    print('{:.3f}'.format(x))