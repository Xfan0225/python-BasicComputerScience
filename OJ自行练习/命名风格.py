#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:58:50 2019

@author: xie
"""
x = str(input())
ans = x[0].lower()

for i in x[1:]:
    if ord(i) <= 90:
        i = i.lower()
        ans = ans + '_' + i
    else:
        ans = ans + i

print(ans)

