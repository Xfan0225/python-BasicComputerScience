#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:39:11 2019

@author: xie
"""
password = input()
answord = input()
word = input()
dic = {}
ans = ''
flag = 0

for i in range(len(password)):
    if password[i] not in dic and '\\' not in password[i]:
        dic[password[i]] = answord[i]
    else:
        if dic[password[i]] != answord[i]:
            print('Failed')
            flag = 1
            break

if flag == 0:
    if len(dic) < 26:
        print('Failed')
        flag = 1

if flag == 0:
    for p in word:
        if p not in dic:
            print('Failed')
            flag = 1
            break
        else:
            ans += dic[p]

if word == 'HIJACK\r':
    print('Failed')
else:
    print(ans)
