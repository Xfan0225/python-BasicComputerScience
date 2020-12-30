#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 23:05:42 2019

@author: xie
超级慢……最好别用
"""
a,b = map(int,input().split())
ls = []
ans = 0

for i in range (2,b):
    ls.append(i)            #构造要筛选的数表

for m in range(1000):       #第一个循环 m 是对数表中的第1，2，3，4……m项循环，1000只是一个比较大的数
    for t in ls[m:]:        #第二个循环是从数表中的第m+1项开始到最后一项，每一项与第m项相除
        if t % ls[m-1] == 0 and t/ ls[m-1] != 1:        #当可以整除且商不为1时
            ls.remove(t)    #则不是质数，从列表中移除，这样最终剩下的就是质数了


for z in ls:
    if z >= a:
        ans += z
    elif z > b:
        break
    else:
        continue

print(ans)
