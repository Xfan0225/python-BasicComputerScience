#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:34:32 2019

@author: xie
"""
#计算样条插值
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
x0=[0, 3, 5, 7, 9, 11, 12, 13, 14, 15];  #输入离散的观测值
y0=[0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6];
x=np.linspace(0,15,101)
plt.plot(x0, y0, '+',color='red',label=u"原始数据")#显示观察值
l=interpolate.lagrange(x0,y0);#计算拉格朗日插值
y1=l(x)
plt.plot(x,y1,color='blue',label=u"拉格朗日插值")

#计算三次样条插值
t = interpolate.splrep(x0,y0);
y2=interpolate.splev(x,t)
plt.plot(x,y2,color='green',label=u"三次样条插值")
t = interpolate.splrep(x0,y0);
y2=interpolate.splev(x,t)

