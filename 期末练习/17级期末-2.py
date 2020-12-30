#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 19:18:33 2019

@author: xie
"""

a, b, c = map(int, input().split())
print('%.3f'%((-b-(b**2-4*a*c)**0.5)/(2*a)))
print('%.3f'%((-b+(b**2-4*a*c)**0.5)/(2*a)))