#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:33:06 2019

@author: xie
"""

n1,n2,n3=map(int,(input().split()))

sum1 = 0
sum2 = 0
sum3 = 0

for i in range(n1):
    sum1 = sum1 + int(input())
if sum1 > 15:
    sum1 = 15

for t in range(n2):
    sum2 = sum2 + int(input())
if sum2 > 15:
    sum2 = 15
    
for p in range(n3):
    sum3 = sum3 + int(input())
if sum3 > 15:
    sum3 = 15
    
print(sum1+sum2+sum3)