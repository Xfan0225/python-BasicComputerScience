#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:54:34 2019

@author: xie
"""

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def lagrange(n,x):
    ans = 0
    for k in range(n+1):
        val = 1
        for i in range(n+1):
            if i != k:
                val *= np.poly1d([1,-x[i]])/(x[k]-x[i])
        ans += f(x[k])*val
    return np.poly1d(ans)

x = np.linspace(-1,1,1000)
x0 = np.linspace(-1,1,6)
x1 = np.linspace(-1,1,11)
x2 = np.linspace(-1,1,16)

def f(x):
    return 1/(36*(x**2)+1)

y = f(x)
y0 = f(x0)
y1 = f(x1)
y2 = f(x2)

l0 = lagrange(5,x0)
l1 = lagrange(10,x1)
l2 = lagrange(15,x2)

plt.plot(x,y,'r',label = 'f(x)')
plt.plot(x,l0(x),color = (0, 0.5, 0, 1),label = '$L_5(x)$')
plt.plot(x,l1(x),color = (0, 0.5, 0, 0.8),label = '$L_{10}(x)$')
plt.plot(x,l2(x),color = (0, 0.5, 0, 0.6),label = '$L_{15}(x)$')
plt.legend()
plt.title('18377039 '+u'谢纪帆',FontProperties=font)

print('L5(x) = ')
print(l0)
print('------------------------------------------------------------------')
print('L10(x) = ')
print(l1)
print('------------------------------------------------------------------')
print('L15(x) = ')
print(l2)
print('------------------------------------------------------------------')
