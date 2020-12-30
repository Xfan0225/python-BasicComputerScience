#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:26:51 2019

@author: xie
"""

word = input().lower()
arti = input().split()
ans = 0
for w in arti:
    if w.lower() == word:
        ans += 1
if ans != 0:
    print(ans, end=' ')
    print(arti.index(word))
else:
    print(-1)
