#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:52:13 2019

@author: xie
"""

'''
d = int(input())
dic = {}
ls_x = []
ls_y = []
ls_loc = []
for i in range(129):                #i为x
    for t in range(129):            #t为y
        dic[i, t] = 0

n = int(input())

for i in range(n):
    x, y, k = map(int, input().split())
    ls_x.append(x)
    ls_y.append(y)
    dic[x, y] = k

ans = 0
time = 0

for x1 in range(n):               #对x，y进行遍历
    for y1 in range(n):
        test = 0
        x3 = ls_x[x1]
        y3 = ls_y[y1]
        for x2 in range(0,d*2+1):                 #对x，y点附近的覆盖进行求和
            for y2 in range(0,d*2+1):
                test += dic.get((x3-d+x2,y3-d+y2), 0)
        if test > ans:
            ans = test
            time = 1
        elif test == ans:
            time += 1

print(time, end=' ')
print(ans)
'''

d = int(input())
dic = {}

for i in range(129):                #i为x
    for t in range(129):            #t为y
        dic[i, t] = 0

n = int(input())

for i in range(n):
    x, y, k = map(int, input().split())
    dic[x, y] = k

ans = 0
time = 0

for x1 in range(129):               #对x，y进行遍历
    for y1 in range(129):
        test = 0
        for x2 in range(0,d*2+1):                 #对x，y点附近的覆盖进行求和
            for y2 in range(0,d*2+1):
                test += dic.get((x1-d+x2,y1-d+y2), 0)
        if test > ans:
            ans = test
            time = 1
        elif test == ans:
            time += 1

print(time, end=' ')
print(ans)



