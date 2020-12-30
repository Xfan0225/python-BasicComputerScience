#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:38:58 2019

@author: xie
"""
def main(x):
    ans = 1
    if x == 1:
        print(ans)
     else:
        ans = main(x-1) + 1
        return x-1
    
main()