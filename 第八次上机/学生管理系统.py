#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:38:16 2019

@author: xie
"""


from tkinter.messagebox import showinfo
from tkinter import *

TeacherAccount = {'admin':{'Pwd':'123456',
                           'Name':'Admin'},
                  'admin2':{'Pwd':'987654321',
                            'Name':'Admin2'}}

StudentList = {'BZB':100,
               'bzb':90,
               'Bzb':80}

def exit_top():
    top.destroy()

def exit_man():
    manage.man.destroy()

def exit_add():
    add.InpStu.destroy()

def login():
    global TeacherAccount
    name = text_name.get()
    password = text_password.get()
    dic = TeacherAccount
    if name not in dic.keys():
        messagebox.showinfo('登录失败','用户名或密码错误')
    elif password == dic[name]['Pwd']:
        messagebox.showinfo('登陆成功,','欢迎'+str(dic[name]['Name']))
        exit_top()
        manage()
    else:
        messagebox.showinfo('登录失败','用户名或密码错误')

def manage():   #控制界面打包的函数
    manage.man = Tk()
    manage.man.title('学生管理系统内部界面')

    #以下为按钮
    add_button = Button(manage.man, text='添加成绩', command = add)
    view_button = Button(manage.man, text='查看成绩', command = view_score)
    exit_button = Button(manage.man, text='退出系统', command = exit_man)

    #以下为布局
    add_button.grid_configure(column = 1, row = 1, columnspan = 1, rowspan = 1)
    view_button.grid_configure(column = 1, row = 2, columnspan = 1, rowspan = 1)
    exit_button.grid_configure(column = 1, row = 3, columnspan = 1, rowspan = 1)
    manage.man.mainloop()

def add():   #添加成绩界面打包的函数
    add.InpStu = Tk()
    add.InpStu.title('提示')

    #以下为提示标签
    InpName = Label(add.InpStu, text='请输入学生姓名')
    InpName.grid_configure(column = 1, row = 1, columnspan = 1, rowspan = 1)
    InpScore = Label(add.InpStu, text='请输入学生成绩')
    InpScore.grid_configure(column = 1, row = 2, columnspan = 1, rowspan = 1)

    #以下为按钮
    AddButton = Button(add.InpStu, text='确认添加', command = add_score)
    Exit = Button(add.InpStu, text='结束添加', command = exit_add)
    AddButton.grid_configure(column = 1, row = 3, columnspan = 1, rowspan = 1)
    Exit.grid_configure(column = 2, row = 3, columnspan = 1, rowspan = 1)

    #以下为输入环节
    add.StuScore = Entry(add.InpStu, width = 10)
    add.StuName = Entry(add.InpStu, width = 10)
    add.StuScore.grid_configure(column = 2, row = 2, columnspan = 1, rowspan = 1)
    add.StuName.grid_configure(column = 2, row = 1, columnspan = 1, rowspan = 1)
    add.InpStu.mainloop()

def add_score():
    global StudentList
    stuname = add.StuName.get()
    stuscore = add.StuScore.get()
    if stuname in StudentList.keys():
        messagebox.showinfo('错误', '该学生已经存在')
    else:
        StudentList[stuname] = stuscore
        messagebox.showinfo('添加成功', '成绩已成功添加')

def view_score():
    global StudentList
    dic = StudentList
    for name in dic.keys():
        print('姓名: '+str(name),end = '    ')
        print('成绩: '+str(dic[name]))

#---------主窗口界面----------#
top = Tk()
top.title('学生管理系统登录界面')

#以下为提示标签
name = Label(top, text='用户名：')
password = Label(top, text='密码：')

#以下为输入文本框
text_name = Entry(top, width = 10)
text_password = Entry(top, width = 10, show='*')

#以下为按钮
login_button = Button(top, text='Login', command = login)
exit_button = Button(top, text='退出系统', command = exit_top)

#以下为布局
name.grid_configure(column = 1, row = 1, columnspan = 1, rowspan = 1)
password.grid_configure(column = 1, row = 2, columnspan = 1, rowspan = 1)
text_name.grid_configure(column = 2, row = 1, columnspan = 1, rowspan = 1)
text_password.grid_configure(column = 2, row = 2, columnspan = 1, rowspan = 1)
login_button.grid_configure(column = 1, row = 3, columnspan = 1, rowspan = 1)
exit_button.grid_configure(column = 2, row = 3, columnspan = 1, rowspan = 1)
top.mainloop()
