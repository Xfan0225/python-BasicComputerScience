#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:11:01 2019

@author: xie
"""

val1 = str(input()).lower()
val2 = str(input()).lower()
num1 = ord(val1)
num2 = ord(val2)
if num1 != num2:
    ans = abs(abs(num1 - num2)-1)
    print(ans)
else:
    print('0')

