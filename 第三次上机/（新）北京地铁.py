#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:13:03 2019

@author: xie
"""
ans = 0
ans1 = 0
ans2 = 0
ans3 = 0
ls = []

n1, n2, n3 = map(int, input().split())

for i in range(n1):
    ans1 = ans1 + int(input())

for t in range(n2):
    ans2 = ans2 + int(input())

for p in range(n3):
    ans3 = ans3 + int(input())

ls.append(ans1+ans2+ans3)
ls.append(40)
ls.append(20+ans2+ans3)
ls.append(ans1+ans3+20)
ls.append(ans2+ans1+20)
ls.append(30+ans1)
ls.append(30+ans3)

print(min(ls))
