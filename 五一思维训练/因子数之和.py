#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 16:16:28 2019

@author: xie
"""
import math
#import time

#start=time.perf_counter()

def make(n):                #计算因子数的函数
    ans = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 2
    else:
        for i in range(1, math.ceil(n**0.5)):
            if n % i == 0:          #假如可以被整除，则肯定有其和其对应的因子，因子数+2
                ans += 2
        if n**0.5 == math.floor(n**0.5):
            ans += 1                #假如是平方数，则因子数为平方项+1
        return ans

n = int(input())
ans = 0

for i in range(1, n+1):
    ans += make(i)

print(ans)

#end=time.perf_counter()

#print(end-start)
