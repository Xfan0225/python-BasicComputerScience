#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:20:09 2019

@author: xie
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ji_a = 0
ji_b = 0
for i in a:
    if i % 2 == 1:
        ji_a += 1

for i in b:
    if i % 2 == 1:
        ji_b += 1

ou_a = n - ji_a
ou_b = n - ji_b
print(min(ji_a,ou_b)+min(ji_b,ou_a))
