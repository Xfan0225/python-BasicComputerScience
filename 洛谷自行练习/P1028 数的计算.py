#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:10:42 2019

@author: xie
"""

n = int(input())
ls = [1]
for i in range(n):
    ls.append(1)
for i in range(1,n+1):
    for j in range(1,i//2+1):
        ls[i] = ls[i] + ls[j]

print(ls[n])

'''
n = int(input())
ans = 0
def make(n):
    global ans
    if n == 1:
        ans += 1

    else:
        for i in range(n//2):
            ans += 1
            make(i)

make(n)
print(ans)
'''

'''
ans = 0
def create(n, m): #n是输入的数，m是添加的正整数允许的最大值
    global ans
    if n == 1:
        ans += 1
        return

    else:
        m = n // 2  #m为n整除2的数
        for i in range(1, m+1): #对1 到 m 每一个i相当于一个新的n，上限为m
            ans += 1
            if i != 1:
                create(i, m)
    return(ans)

n = int(input())
if n == 1:
    print(1)
else:
    print(create(n,n)+1)
'''