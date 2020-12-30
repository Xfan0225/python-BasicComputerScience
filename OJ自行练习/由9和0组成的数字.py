#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:39:45 2019

@author: xie
"""
'''
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
'''

ls = [9]
mod = int(input())
n = 1
flag = 0

while True:
    if flag == 1:
        break
    lenth = len(ls)
    ls.append(9*(10**n))
    for t in range(lenth):
        ls.append(9*(10**n) + ls[t])
    n += 1
    for i in ls:
        if i % mod == 0:
            print(i)
            flag = 1
            break
