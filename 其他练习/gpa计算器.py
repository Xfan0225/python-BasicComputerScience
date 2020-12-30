#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:31:45 2019

@author: xie
"""

print("x帆自己写的辣鸡成绩计算系统，仅作为面向对象编程的一个小测试")
print("-------------使用方法-------------")
print("请在一行内输入您的成绩，该门课程所占学分。用空格分割")
print("如输入完成，请输入-1 -1作为结束标志")
print("-------------说明结束，您可以开始使用了-------------")

gpadic = {60: 1.000, 61: 1.148, 62: 1.292, 63: 1.433, 64: 1.570, 65: 1.703,
          66: 1.833, 67: 1.958, 68: 2.080, 69: 2.198, 70: 2.312,
          71: 2.423, 72: 2.530, 73: 2.633, 74: 2.732, 75: 2.828,
          76: 2.920, 77: 3.008, 78: 3.093, 79: 3.173, 80: 3.250,
          81: 3.323, 82: 3.393, 83: 3.458, 84: 3.520, 85: 3.578,
          86: 3.632, 87: 3.683, 88: 3.730, 89: 3.773, 90: 3.812,
          91: 3.848, 92: 3.880, 93: 3.908, 94: 3.933, 95: 3.953,
          96: 3.970, 97: 3.983, 98: 3.993, 99: 3.998, 100:4.000}

sum_credit = 0
sum_score = 0
sum_credit_score = 0
sum_course = 0
sum_gpa = 0

class make():
    def __init__(self, score, credit):
        self.score = score
        self.credit = credit

    def add_score(self, sum_credit=0, sum_score=0, sum_gpa=0, sum_course=0, sum_credit_score=0):
        self.sum_credit = self.credit+sum_credit
        self.sum_score = self.score+sum_score
        self.sum_credit_score = self.credit*self.score + sum_credit_score
        self.sum_course = 1+sum_course
        self.sum_gpa = sum_gpa + gpadic.get(self.score, 0)*self.credit
        return self.sum_credit, self.sum_score, self.sum_gpa, self.sum_course, self.sum_credit_score

    def cal_raw_avg(self, raw_avg=0):
        return (self.sum_score)/(self.sum_course)

    def cal_cal_avg(self, cal_avg=0):
        return (sum_credit_score)/(self.sum_credit)

    def cal_gpa(self, sum_gpa=0):
        return (self.sum_gpa)/(self.sum_credit)

while True:
    sc, cd = map(eval, input().split())
    if sc == -1 and cd == -1:
        break
    elif sc < 0 or sc > 100 or cd < 0:
        print('输入有误请检查')
    else:
        inp = make(sc, cd)
        sum_credit, sum_score, sum_gpa, sum_course, sum_credit_score = inp.add_score(sum_credit, sum_score, sum_gpa, sum_course, sum_credit_score)
        raw = inp.cal_raw_avg()
        cal = inp.cal_cal_avg()
        Calgpa = inp.cal_gpa()

    print("你目前的算数平均分是：{0:.3f},加权平均分是：{1:.3f}, gpa是：{2:.4f}".format(raw ,cal ,Calgpa))
    print("-------------请继续输入-------------")





