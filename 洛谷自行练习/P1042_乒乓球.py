#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 19:09:02 2019

@author: xie
"""
flag = 0
hua11 = 0
li11 = 0
hua21 = 0
li21 = 0
ans11 = []
ans21 = []
while flag == 0:
    text = input()
    for i in text:
        if i == 'W':
            hua11 += 1
            hua21 += 1
            if hua11 >= 11 and hua11-li11 >= 2:
                ans11.append(str(hua11)+':'+str(li11))
                hua11 = 0
                li11 = 0
            if hua21 >= 21 and hua21-li21 >= 2:
                ans21.append(str(hua21)+':'+str(li21))
                hua21 = 0
                li21 = 0
        elif i == 'L':
            li11 += 1
            li21 += 1
            if li11 >= 11 and li11-hua11 >= 2:
                ans11.append(str(hua11)+':'+str(li11))
                hua11 = 0
                li11 = 0
            if li21 >= 21 and li21-hua21 >= 2:
                ans21.append(str(hua21)+':'+str(li21))
                hua21 = 0
                li21 = 0
        elif i == 'E':
            flag = 1
            ans11.append(str(hua11)+':'+str(li11))
            ans21.append(str(hua21)+':'+str(li21))
            break
for t in ans11:
    print(t)
print('')
for p in ans21:
    print(p)
