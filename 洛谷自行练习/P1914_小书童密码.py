#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:01:43 2019

@author: xie
"""

n = int(input())
password = input().lower()
ans = ''
for i in password:
    ans += chr((ord(i)-ord('a') + n) % 26 + ord('a'))
print(ans)
