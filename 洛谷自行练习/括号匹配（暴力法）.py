#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 12:15:02 2019

@author: xie
"""

ls_l = 0
lm_l = 0
ll_l = 0
ls_r = 0
lm_r = 0
ll_r = 0

for i in input():
    if i == '(':
        ls_l += 1
    elif i == '[':
        lm_l += 1
    elif i == '{':
        ll_l += 1
    elif i == ')':
        ls_r += 1
    elif i == ']':
        lm_r += 1
    elif i == '}':
        ll_r += 1

if ls_l == ls_r:
    if lm_l == lm_r:
        if ll_l == ll_r:
            print('True')
else:
    print('False')


