#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:36:55 2019

@author: xie
"""

ls = list(map(str, input().split()))
ans = ''

for t in ls:
    ans = ans+t
ans = list(ans.lower())

newans = []
for letter in ans:
    if letter not in newans:
        newans.append(letter)

print(len(newans))

for i in ls:
    while 'and' in ls:
        ls.remove('and')
    while 'the' in ls:
        ls.remove('the')
    while 'for' in ls:
        ls.remove('for')
    while 'of' in ls:
        ls.remove('of')

for x in ls:
    print((x[0].upper()), end='') 
