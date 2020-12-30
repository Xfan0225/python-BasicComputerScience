#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 13:34:43 2019

@author: xie
"""

n = input()
if n[0] == '-':
    n = n[1:]
    print(-int(n[::-1]))
else:
    print(int(n[::-1]))