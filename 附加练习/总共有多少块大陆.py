#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 10:05:31 2019

@author: xie
"""

'''
ls = []
n = int(input())
ans = 0

for i in range(n+2):
	ls.append(['*'])
for i in range(n+1):
	ls[0].append('*')
	ls[-1].append('*')

for i in range(n):
	land = input()
	for t in land:
		ls[i+1].append(t)
	ls[i+1].append('*')

for i in range(1,n+2):
    for j in range(1,n+1):
        while ls[i][j] == '#':
            if ls[i][j-1] != '#' and ls[i][j+1] != '#' and ls[i+1][j] != '#' and ls[i-1][j] != '#':
                ans += 1
            else:
            	
print(ans)

'''
'''
ls1 = []
for i in range(n+2):
    ls1.append([])
for i in range(n+2):
    for j in range(n+2):
        if ls[i][j] == '#':
            ls1[i].append(j)
    if len(ls1[i]) == 0:
        ls1[i].append(-1)
ls2 = ls1[1]
for t in range(2,n+2):
    for p in range(len(ls1[t])):
        if ls1[t][p] not in ls2:
            if p != 0 and p != len(ls1[t])-1:
                if ls1[t][p-1]+1 != ls1[t][p] and ls1[t][p]+1 != ls1[t][p+1]:
                    ans += 1
            elif ls1[t][0] == -1:
                ans += 1
            elif p == 0:
                if ls1[t][p]+1 != ls1[t][p+1]:
                    ans += 1
            elif p == len(ls1[t])-1:
                if ls1[t][p-1]+1 != ls1[t][p]:
                    ans += 1
    ls2 = ls1[t]
print(ans)
'''

ls = []
n = int(input())
ans = 0

for i in range(n+2):
	ls.append(['*'])
for i in range(n+1):
	ls[0].append('*')
	ls[-1].append('*')

for i in range(n):
	land = input()
	for t in land:
		ls[i+1].append(t)
	ls[i+1].append('*')
	
stack = ls[0]
for i in range(1,n+1):
	flag = 1
	for t in range(n+2):
		if ls[i][t] == '#':
			if ls[i+1][t] == '#':
				flag = 0
			if ls[i][t+1] == '*' and ls[i-1][t] == '*':
				if flag = 1:
					ans += 1
					flag = 1
					
				
				
	
	
	
	
