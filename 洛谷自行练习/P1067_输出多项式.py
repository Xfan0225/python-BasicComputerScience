#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:15:06 2019

@author: xie
"""

n = int(input())
if n != 0:
    ls = input().split()
    ans = ''
    for t in ls[:-2]:
        if int(t) != 0:
            if int(t) != -1:
                if int(t) > 0:
                    if int(t) != 1:
                        ans += '+'+t+'x^'+str(n)
                        n -= 1
                    elif int(t) == 1:
                        ans += '+x^'+str(n)
                        n -= 1
                elif int(t) < 0:
                    ans += t+'x^'+str(n)
                    n -= 1
            else:
                ans += '-x^'+str(n)
                n -= 1
        elif int(t) == 0:
            n -= 1
            continue

    if int(ls[-2]) != 0:
        if int(ls[-2]) != 1:
            if int(ls[-2]) != -1:
                if int(ls[-2]) > 0:
                    ans += '+'+ls[-2]+'x'
                elif int(ls[-2]) < 0:
                    ans += ls[-2]+'x'
            elif int(ls[-2]) == -1:
                ans += '-x'
        elif int(ls[-2]) == 1:
            ans += '+x'

    if int(ls[-1]) != 0:
        if int(ls[-1]) < 0:
            ans += str(ls[-1])
        elif int(ls[-1]) > 0:
            ans += '+' + str(ls[-1])

    if ans[0] == '+':
        print(ans[1:])
    else:
        print(ans)
else:
    print(input())
