#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 20:44:14 2019

@author: xie
"""

def mxdiflg(a1, a2):
    lsa1 = []
    lsa2 = []
    for i in a1:
        lsa1.append(len(i))
    for t in a2:
        lsa2.append(len(t))
    return max(abs(max(lsa1)-min(lsa2)), abs(max(lsa2)-min(lsa1)))

a1, a2 = map(list, input().split(','))
midiflg(a1, a2)
