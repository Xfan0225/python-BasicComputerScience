#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 13:39:08 2019

@author: xie
"""

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception('stackIsEmpty')
        else:
            return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise Exception('stackIsEmpty')
        else:
            return self.items[-1]
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

flag = 0

s=Stack()

for i in input():
    if i in ['(' , '[' , '{']:
        s.push(i)
    elif i in [')',']','}']:
        if i != s.pop():
            flag = 1
            break

if flag == 0:
    print('Ture')
elif flag == 1:
    print('False')