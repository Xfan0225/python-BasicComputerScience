#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:55:33 2019

@author: xie
"""

star = str(input().lower())
team = str(input().lower())
ans_s = 1
ans_t = 1
for i in star:
    ans_s *= ord(i) - ord('a') + 1

for i in team:
    ans_t *= ord(i) - ord('a') + 1

if ans_s % 47 == ans_t % 47:
    print('GO')
else:
    print('STAY')