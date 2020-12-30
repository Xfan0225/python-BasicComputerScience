#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:41:32 2019

@author: xie
"""

h1, m1, h2, m2 = map(int, input().split())
if m2 < m1:
    print(h2-h1-1, end=' ')
    print(60-(m1-m2))
elif m2 >= m1:
    print(h2-h1, end=' ')
    print(m2-m1)
