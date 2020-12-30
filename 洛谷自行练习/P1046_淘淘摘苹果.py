#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 23:48:44 2019

@author: xie
"""

ls = input().split()
lenth = int(input())
ans = 0

for i in ls:
    if int(i) - lenth <= 30:
        ans += 1

print(ans)
