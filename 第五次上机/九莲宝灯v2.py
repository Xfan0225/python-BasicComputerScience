#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:37:03 2019

@author: xie
"""
#ac代码：1637328
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
flag = 0
for a in ls:
    time += 1
    if a[-1] == 'm':
        lsm.append(int(a[0]))
    elif a[-1] == 's':
        lss.append(int(a[0]))
    elif a[-1] == 'p':
        lsp.append(int(a[0]))

    if lsm.count(1) >= 3:
        if lsm.count(2) >= 1:
            if lsm.count(3) >= 1:
                if lsm.count(4) >= 1:
                    if lsm.count(5) >= 1:
                        if lsm.count(6) >= 1:
                            if lsm.count(7) >= 1:
                                if lsm.count(8) >= 1:
                                    if lsm.count(9) >= 3:
                                        if len(lsm) >= 14:
                                            print(time)
                                            flag = 1
                                            break
    if lss.count(1) >= 3:
        if lss.count(2) >= 1:
             if lss.count(3) >= 1:
                  if lss.count(4) >= 1:
                       if lss.count(5) >= 1:
                            if lss.count(6) >= 1:
                                 if lss.count(7) >= 1:
                                      if lss.count(8) >= 1:
                                           if lss.count(9) >= 3:
                                               if len(lss)>= 14:
                                                   print(time)
                                                   flag = 1
                                                   break

    if lsp.count(1) >= 3:
        if lsp.count(2) >= 1:
            if lsp.count(3) >= 1:
                if lsp.count(4) >= 1:
                    if lsp.count(5) >= 1:
                        if lsp.count(6) >= 1:
                            if lsp.count(7) >= 1:
                                if lsp.count(8) >= 1:
                                    if lsp.count(9) >= 3:
                                        if len(lsp) >= 14:
                                            print(time)
                                            flag = 1
                                            break

if flag == 0:
    print('Stop Your Daydream!')


