# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = int(input())
dict_1 = {}
for i in range(n):
    a, b, g, k = map(int, input().split())
    for t in range(a, a+g):
        for x in range(b, b+k):
            dict_1[t, x] = i+1

x, y = map(int, input().split())
if (x, y) in dict_1:
    print(dict_1[(x, y)])
else:
    print('-1')
