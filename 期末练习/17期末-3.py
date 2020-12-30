#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:30:54 2019

@author: xie
"""

n = input().lower()
word = n.split()
p = str(word[0])
word[0] = p[0].upper()+p[1:]
for i in range(len(word)):
    if word[i] == 'i':
        word[i] = 'I'
    elif word[i] == 'i.':
        word[i] = 'I.'
for t in word:
    print(t,end=' ')

