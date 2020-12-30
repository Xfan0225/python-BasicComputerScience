#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:07:21 2019

@author: xie
"""

l, r = map(int, input().split())
ans = 0

for x in range(l, r):                       #对l-r中的数字进行循环
    ans1 = 0
    ans2 = 0

    for p in range(1, x//2+1):                    #对循环的数字x求因数和
        if x % p == 0:                          #如果p是x的因数
            ans1 += p                           #则对p求和,ans1是x质因数的和

    for t in range(1, ans1//2+1):                 #对x的因数的和进行一次相同循环
        if ans1 % t == 0:
            ans2 += t

    if ans2 == x:                               #假如x质因数的和等于其质因数的和的质因数的和
        if ans1>= l and ans1 <= r and ans1 != x:
            ans += ans1 + x
            #print(ans1)
            #print(x)
print(int(ans/2))
