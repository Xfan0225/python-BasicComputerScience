#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:29:35 2019

@author: xie
"""
# 其中 0 表示朝向圈内，1 表示朝向圈外。
# 0 向左数 1 向右数
# 0,0 倒走 1，1 倒走 10 01正走
n, m = map(int, input().split())
ls_dir = []
ls_job = []
time = 0

for i in range(n):
    direct, job = input().split()
    ls_dir.append(int(direct))
    ls_job.append(job)

for p in range(m):
    d, t = map(int, input().split())
    if ls_dir[time % n] == 0:
        if d == 0:
            if time-t < 0 and abs(time-t) >= n:
                ans = ls_job[-((time-t) % n)]
                time -= t
            else:
                ans = ls_job[(time-t) % n]
                time -= t
        elif d == 1:
            if time+t < 0 and abs(time+t) >= n:
                ans = ls_job[-((time+t) % n)]
                time += t
            else:
                ans = ls_job[(time+t) % n]
                time += t
    elif ls_dir[time % n] == 1:
        if d == 0:
            if time+t < 0 and abs(time+t) >= n:
                ans = ls_job[-((time+t) % n)]
                time += t
            else:
                ans = ls_job[(time+t) % n]
                time += t
        elif d == 1:
            if time-t < 0 and abs(time-t) >= n:
                ans = ls_job[-((time-t) % n)]
                time -= t
            else:
                ans = ls_job[(time-t) % n]
                time -= t
    #print(ans)
    #print(time)
print(ans)

