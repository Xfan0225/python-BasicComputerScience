#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:51:46 2019

@author: xie
"""

ls = list(map(float, input().split()))  #周一到周日的概率
ls1 = []                                #周一到周日的1-概率（没来的概率）
for t in ls:
    ls1.append(1-t)

i = 1
ans = 0
while True:
    p = 1
    if i > 1:
        for s in range(i-1):
            p *= ls1[s%7]                   #对于第i次来了的概率，先乘i-1次没来的概率
        p *= ls[(i-1)%7]                        #再乘第i次来了的概率
    elif i == 1:
        p == ls[0]
    if i*p <= 0.0000000001:                 #如果这个概率过于小（在精度范围内）
        print('{:.8f}'.format(ans-ls1[0]))     #输出结果(为啥要减去那个数我没想明白)
        break
    else:
        ans += i*p                          #否则将结果累加且次数+1
    i += 1
