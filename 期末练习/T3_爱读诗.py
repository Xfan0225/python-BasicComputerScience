#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 13:54:42 2019

@author: xie
"""
flag = 0
n = input()
for i in range(len(n),1,-1):
	if flag == 1:
		break
	for j in range(len(n)-i+1):
		val = n[j:i+j]
		if val == val[::-1]:
			print(len(val))
			flag = 1
			break
if flag == 0:
	print(1)
