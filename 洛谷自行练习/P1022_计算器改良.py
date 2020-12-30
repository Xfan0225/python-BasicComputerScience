#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:23:08 2019

@author: xie
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
n = input()
num = 0
var = 0
flag = 1
eqt = 0
val = ''
cal = ''
ls = []
for k in n:
    ls.append(k)
for a in ls:
    if ord(a) >= ord('a') and ord(a) <= ord('z'):
        val = a
while len(ls) != 0:
    a = ls.pop(0)
    if a == '=':
        eqt = 1
    elif a == val:
        var += 1
    else:
        cal += str(a)
        if len(ls) != 0 and ls[0] == val and cal == '-':
            if eqt == 0:
                var -= 1
            elif eqt == 1:
                var += 1
            ls.pop(0)
            cal = ''
        elif len(ls) != 0 and ls[0] == val and cal == '+':
            if eqt == 0:
                var += 1
            elif eqt == 1:
                var -= 1
            ls.pop(0)
            cal = ''
        else:
            while len(ls) != 0 and is_number(ls[0]):
                if len(ls) != 0:
                    cal += str(ls.pop(0))
            else:
                if len(ls) != 0:
                    if ls[0] == val:
                        if eqt == 0:
                            var += int(cal)

                        elif eqt == 1:
                            var -= int(cal)
                        ls.remove(val)
                        cal = ''
                    else:
                        if eqt == 0:
                            num += int(cal)
                        elif eqt == 1:
                            num -= int(cal)
                        cal = ''
                else:
                    if eqt == 0:
                        num += int(cal)
                    elif eqt == 1:
                        num -= int(cal)
                    cal = ''
print(str(val)+'='+'{:.3f}'.format(num/-var))
