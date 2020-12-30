#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:53:50 2019

@author: xie
"""

import matplotlib.pyplot as plt
import numpy as np


x0 = []
y0 = []
ls = [(1, 0),(1.2, 3.064), (1.4, 3.594), (1.46, 3.439), (1.65, 2.417), (1.89, 0.713), (2, 0), (2.35, -1.342), (2.47, -1.417), (2.59, -1.306), (2.78, -0.827), (2.9, -0.395), (3, 0), (3.29, 1.04), (3.48, 1.392), (3.69, 1.273), (3.91, 0.496), (4, 0), (4.19, -1.279), (4.44, -2.978), (4.68, -3.605), (4.87, -2.349), (5, 0)]
for item in ls:
    x0.append(item[0])
    y0.append(item[1])

plt.plot(x0,y0, 'ro--', label='original line', linewidth = '1')
plt.legend()

x1 = np.linspace(1, 5, 1000)
cal = np.poly1d(np.polyfit(x0 ,y0, 5))
y1 = cal(x1)
plt.plot(x1,y1, 'b', label='smooth line', linewidth = '2' )
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
