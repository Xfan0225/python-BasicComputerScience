#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:02:52 2019

@author: xie
"""
x1,y1 = map(eval,input().split())
a , b , c = map(eval,input().split())
d = abs((a*x1+b*y1+c)/(a**2+b**2)**0.5)
print('{:.3f}'.format(d))
