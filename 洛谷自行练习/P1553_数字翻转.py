#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:37:20 2019

@author: xie
"""

n = input()
for i in n:
    if i == '.':
        flag = 1
        break
    elif i == '/':
        flag = 2
        break
    elif i == '%':
        flag = 3
        break
    else:
        flag = 0

ls = []
if flag == 0:
    print(int(str(n)[::-1]))
elif flag == 1:
    ls = n.split('.')
    print(int(str(ls[0])[::-1]), end = '.')
    if int(ls[1]) != 0:
        print(int(str(ls[1])[::-1].strip('0')))
    else:
        print(0)
elif flag == 2:
    ls = n.split('/')
    print(int(str(ls[0])[::-1]), end = '/')
    print(int(str(ls[1])[::-1]))
elif flag == 3:
    print((int(str(n)[:-1][::-1])), end = '%')
