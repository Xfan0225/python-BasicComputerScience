#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 23:24:47 2019

@author: xie
"""
n = int(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i,n))

for t in range(1,n,2):
    print('{0:^{1}}'.format('*'*(n-t-1),n))
    
 