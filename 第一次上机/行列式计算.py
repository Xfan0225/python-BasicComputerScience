#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 16:23:42 2019

@author: xie
"""

a11,a12,a13 = map(eval,input().split())
a21,a22,a23 = map(eval,input().split())
a31,a32,a33 = map(eval,input().split())
ans = (a11*a22*a33+a12*a23*a31+a13*a21*a32-a13*a22*a31-a12*a21*a33-a11*a23*a32)
print(ans)