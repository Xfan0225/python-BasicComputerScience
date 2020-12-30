#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:35:50 2019

@author: xie
"""

hand = input()
come = input()
ls = []
for i in range(0,26,2):
    ls.append(hand[i]+hand[i+1])
for t in range(0,34,2):
    ls.append(come[t]+come[t+1])

lsm = []
lss = []
lsp = []

time = -13
timem1 = 0
timem9 = 0
times1 = 0
times9 = 0
timep1 = 0
timep9 = 0

for a in ls:
    time += 1
    if a[-1] == 'm':
        if len(lsm) == 13:
            lsm.append(int(a[0]))
        else:
            if int(a[0]) not in lsm:
                lsm.append(int(a[0]))
            elif int(a[0]) == 1 and timem1 < 2:
                lsm.append(int(a[0]))
                timem1 += 1
            elif int(a[0]) == 9 and timem9 < 2:
                lsm.append(int(a[0]))
                timem9 += 1
    elif a[-1] == 's':
        if len(lss) == 13:
            lss.append(int(a[0]))
        else:
            if int(a[0]) not in lss:
                lss.append(int(a[0]))
            elif int(a[0]) == 1 and times1 < 2:
                lss.append(int(a[0]))
                times1 += 1
            elif int(a[0]) == 9 and times9 < 2:
                lss.append(int(a[0]))
                times9 += 1
    elif a[-1] == 'p':
        if len(lsp) == 13:
            lsp.append(int(a[0]))
        else:
            if int(a[0]) not in lsp:
                lsp.append(int(a[0]))
            elif int(a[0]) == 1 and timep1 < 2:
                lsp.append(a[0])
                timep1 += 1
            elif int(a[0]) == 9 and timep9 < 2:
                lsp.append(int(a[0]))
                timep9 += 1

    if len(lsm) == 14 or len(lss) == 14 or len(lsp) == 14:
        print(time)
        break

if len(lsm) < 14 and len(lss) < 14 and len(lsp) < 14:
    print('Stop Your Daydream!')



