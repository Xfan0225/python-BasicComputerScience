#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:40:02 2019

@author: xie
"""
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

#from pylab import mpl
#mpl.rcParams['font.sans-serif'] = ['PingFang']
data = input().lower()
dic = {}

for i in range(ord('a'),ord('z')+1):
    dic[chr(i)] = 0

for i in data:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        dic[i] += 1

for i in dic:
    print(i, end=' ')
    print(dic[i])

plt.bar(dic.keys(),dic.values())

plt.xlabel(u'分类',FontProperties=font)
plt.ylabel(u'数字',FontProperties=font)
