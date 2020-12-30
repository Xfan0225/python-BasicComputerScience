#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:01:10 2019

@author: xie
"""

n, na, nb = map(int, input().split())
ls_a = input().split()
ls_b = input().split()
ans_a = []
ans_b = []
sum_a = 0
sum_b = 0

for i in range(n):
    ans_a.append(ls_a[i % len(ls_a)])

for t in range(n):
    ans_b.append(ls_b[t % len(ls_b)])

for m1 in range(len(ans_a)):
    ans_a[m1] = int(ans_a[m1])

for m2 in range(len(ans_b)):
    ans_b[m2] = int(ans_b[m2])

time = -1

for x in ans_a:
    time += 1
    if x == 0:
        if ans_b[time] == 1:
            sum_b += 1
        elif ans_b[time] == 2:
            sum_a += 1
        elif ans_b[time] == 3:
            sum_a += 1
        elif ans_b[time] == 4:
            sum_b += 1

    elif x == 1:
        if ans_b[time] == 0:
            sum_a += 1
        elif ans_b[time] == 2:
            sum_b += 1
        elif ans_b[time] == 3:
            sum_a += 1
        elif ans_b[time] == 4:
            sum_b += 1

    elif x == 2:
        if ans_b[time] == 0:
            sum_b += 1
        elif ans_b[time] == 1:
            sum_a += 1
        elif ans_b[time] == 3:
            sum_b += 1
        elif ans_b[time] == 4:
            sum_a += 1

    elif x == 3:
        if ans_b[time] == 0:
            sum_b += 1
        elif ans_b[time] == 1:
            sum_b += 1
        elif ans_b[time] == 2:
            sum_a += 1
        elif ans_b[time] == 4:
            sum_a += 1

    elif x == 4:
        if ans_b[time] == 0:
            sum_a += 1
        elif ans_b[time] == 1:
            sum_a += 1
        elif ans_b[time] == 2:
            sum_b += 1
        elif ans_b[time] == 3:
            sum_b += 1

print(sum_a, end=' ')
print(sum_b)
