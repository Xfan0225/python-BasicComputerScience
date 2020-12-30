#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:38:58 2019

@author: xie
"""

#通过编码：1637879
ls = []
d = int(input())
n = int(input())
ans = 0
time = 0
for i in range(129):
    ls.append([0]*129)

for i in range(n):
    x, y, k = map(int, input().split())
    ls[x][y] = k

for x1 in range(129):
    for y1 in range(129):
        test = 0
        for x2 in range(0 if x1-d < 0 else x1-d, 129 if x1+d > 128 else x1+d+1):
            for y2 in range(0 if y1-d < 0 else y1-d, 129 if y1+d > 128 else y1+d+1):
                test += ls[x2][y2]
        if test > ans:
            ans = test
            time = 1
        elif test == ans:
            time += 1

print(time, end=' ')
print(ans)