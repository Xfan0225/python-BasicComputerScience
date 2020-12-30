#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:53:36 2019

@author: xie
"""


save = 0
hand = 0
flag = 0
for i in range(12):
    budget = int(input())
    hand += 300-budget
    if hand < 0 and flag == 0:
        gg = -(i+1)
        flag = 1
    else:
        if hand >= 100:
            q = hand // 100
            save += q*100
            hand -= q*100

if flag == 0:
    print(int(save*1.2 + hand))
elif flag == 1:
    print(gg)
