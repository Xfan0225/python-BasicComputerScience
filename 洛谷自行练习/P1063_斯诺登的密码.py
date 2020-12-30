#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:26:27 2019

@author: xie
"""

numls = 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
numls2 = {'a':1 ,'both':2, 'another':2, 'first':2, 'second':2, 'third':3}
ls = input().lower().split()
ansls = []
for i in ls:
    if i in numls:
        num = numls.index(i)+1
        num = (num**2)%100
        ansls.append(num)
    elif i in numls2:
        num = numls2[i]
        num = (num**2)%100
        ansls.append(num)
ansls.sort()
ans = ''
for i in ansls:
    if i < 10:
        ans += '0'+str(i)
    else:
        ans += str(i)
if len(ansls) == 0:
    print(0)
else:
    print(int(ans))