#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:54:57 2019

@author: xie
"""

ls = list(input().split())
stack = []
alpha = []
for i in range(ord('a'),ord('z')+1):
    alpha.append(chr(i))
for i in ls:
    if i in alpha:
        stack.append(i)
    elif i in ['+','-','*','/']:
        a = stack.pop(-1)
        b = stack.pop(-1)
        stack.append(i+str(b)+str(a))
for p in stack[-1]:
    print(p,end = ' ')

