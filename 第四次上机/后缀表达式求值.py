#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:21:08 2019

@author: xie
"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

stack = []
ls = input().split()
for i in ls:
    if is_number(i):
        i = float(i)
        stack.append(i)
    elif i == '+':
        ele1 = stack.pop(-2)
        ele2 = stack.pop(-1)
        stack.append(ele1+ele2)
    elif i == '-':
        ele1 = stack.pop(-2)
        ele2 = stack.pop(-1)
        stack.append(ele1-ele2)
    elif i == '*':
        ele1 = stack.pop(-2)
        ele2 = stack.pop(-1)
        stack.append(ele1*ele2)
    elif i == '/':
        ele1 = stack.pop(-2)
        ele2 = stack.pop(-1)
        stack.append(ele1/ele2)
ans = stack[-1]
print('{:.2f}'.format(ans))