#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:43:32 2019

@author: xie
"""
import math

budget = int(input())
N = int(input())

sum = 0
for i in range(N):
    money = float(input())
    if money >= 200:
        money = money - 40
    elif money >= 100:
        money = money - 15
    elif money >= 50:
        money = money - 5
    elif money < 50:
        money = money
    sum = sum + money

if sum >= 1000:
    sum = math.floor(sum*0.8)
elif sum >= 500:
    sum = math.floor(sum*0.9)
else:
    sum = math.floor(sum)

if sum <= budget:
    print(int(sum))
    print('enough!')
elif sum > budget:
    print(int(sum))
    print('chitu!')