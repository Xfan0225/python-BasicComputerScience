#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:44:06 2019

@author: xie

文件存放地址：/Users/xie/indata.txt
"""

#等待实现目标：高亮文本，书签功能

#---大学计算机基础大作业————文本处理程序---#

from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
showflag = 0
execludes = ['very', 'ourselves', 'am', 'doesn', 'through', 'me', 'against', 'up', 'just', 'her', 'ours',
            'couldn', 'because', 'is', 'isn', 'it', 'only', 'in', 'such', 'too', 'mustn', 'under', 'their',
            'if', 'to', 'my', 'himself', 'after', 'why', 'while', 'can', 'each', 'itself', 'his', 'all', 'once',
            'herself', 'more', 'our', 'they', 'hasn', 'on', 'ma', 'them', 'its', 'where', 'did', 'll', 'you',
            'didn', 'nor', 'as', 'now', 'before', 'those', 'yours', 'from', 'who', 'was', 'm', 'been', 'will',
            'into', 'same', 'how', 'some', 'of', 'out', 'with', 's', 'being', 't', 'mightn', 'she', 'again', 'be',
            'by', 'shan', 'have', 'yourselves', 'needn', 'and', 'are', 'o', 'these', 'further', 'most', 'yourself',
            'having', 'aren', 'here', 'he', 'were', 'but', 'this', 'myself', 'own', 'we', 'so', 'i', 'does', 'both',
            'when', 'between', 'd', 'had', 'the', 'y', 'has', 'down', 'off', 'than', 'haven', 'whom', 'wouldn',
            'should', 've', 'over', 'themselves', 'few', 'then', 'hadn', 'what', 'until', 'won', 'no', 'about','tis'
            'any', 'that', 'for', 'shouldn', 'don', 'do', 'there', 'doing', 'an', 'or', 'ain', 'hers', 'wasn',
            'weren', 'above', 'a', 'at', 'your', 'theirs', 'below', 'other', 'not', 're', 'him', 'during', 'which','t']

def on_closing():
    if messagebox.askokcancel("警告", "您确认要退出程序嘛？"):
        messagebox.showinfo('再见','感谢您的使用，再会')
        main.top.destroy()

def New():      #关闭旧界面，重新打开
    clean()
    main.top.destroy()
    inpname()

def replace_word():
    global showflag
    global words
    inp = Replace.InpEntry.get()
    otp = Replace.OutEntry.get()
    get_text()
    if inp not in words:
        messagebox.showerror('错误','替换词不存在，请确认后重新输入')
    elif len(words) >= 2000:    #文本长度过长后tkinker处理过慢，故只能在console中展示
        newwords = [otp if i == inp else i for i in words]      #创建一个新列表，假如与替换词重复则采用新的替换词
        allwords = ''
        for i in newwords:
            allwords += i+' '
        words = newwords
        print(allwords)
        showflag = 1
        messagebox.showwarning('提示','文章过长，在文本框中展示过慢，替换后的文本将在Console中展示')
        Replace.rp.destroy()
    else:
        newwords = [otp if i == inp else i for i in words]
        words = newwords
        show_all_words()
        messagebox.showinfo('成功','替换成功')
        Replace.rp.destroy()

def add_word():     #添加停用词函数
    global execludes
    addls = addstop.add.AddEntry.get().split()
    for stopword in addls:
        execludes.append(stopword)
    messagebox.showinfo('成功','添加成功')
    addstop.add.destroy()

def get_file():     #打开文件函数
    inpname.file_name.delete(0,END)
    name = filedialog.askopenfilename()
    inpname.file_name.insert('insert',name)

mode_flag = 0
def protect_mode():     #护眼模式控制函数
    global mode_flag
    if mode_flag == 0:
        main.TextBox.configure(bg='#F7F1E4',fg='#4B3320')
        main.ProtectButton.configure(text='关闭护眼模式')
        mode_flag = 1
    elif mode_flag == 1:
        main.TextBox.configure(bg='#fffffc',fg='black')
        main.ProtectButton.configure(text='开启护眼模式')
        mode_flag = 0

def get_text():     #获取并且处理文本框文章的函数
    global txt
    global words
    if showflag == 0:
        txt = main.TextBox.get(0.0, END)
        txt = txt.lower()       #先全部小写
        for i in '!@#$%^&，。、；‘’：“”【】]*()_+-={}[]:";,./?><1234567890|\'':    #再把特殊符号替换为空格
            txt = txt.replace(i, ' ')
        words = txt.split()
    else:
        pass

def clean(): #清空输入界面
    global showflag
    main.TextBox.delete(1.0,END)
    words = []
    showflag = 0

def draw(wordls,countls):   #绘图函数
    plt.bar(wordls,countls)
    plt.xlabel(u'单词',FontProperties=font)
    plt.ylabel(u'词频',FontProperties=font)
    plt.savefig('./test.png')
    plt.close()

def del_execlude():     #添加停用词
    global execludes
    for e in execludes:
        if e in count.keys():
            del(count[e])

def make_show_dict():   #创建展示字典
    global wordls
    global countls
    del_execlude()  #从词典中删除停用词
    items = list(count.items())
    items.sort(key=lambda x:x[1], reverse=True)
    wordls = []
    countls = []
    for i in range(min(6,len(count))):
        wd, ct = items[i]
        wordls.append(wd)
        countls.append(ct)

def make_count_dict():  #更新词频统计词典
    global count
    get_text()
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    make_show_dict()

def make_temp_dict():   #未采用停用词的词典
    global count
    get_text()      #实时取得文本框的输入
    count = {}      #创建词典进行词频统计
    for w in words:     #统计词频主函数
        count[w] = count.get(w, 0) + 1

def counts():       #词频统计函数
    make_count_dict()
    draw(wordls,countls)
    ShowCountResult()

def ShowCountResult():  #展示词频统计结果界面
    get_text()
    val = ''
    t = 0

    for i in wordls:    #格式化文本函数，将词频统计结果打包成一个字符串进行insert
        val += i
        for s in range(20-len(i)):
            val += ' '
        val += str(countls[t])
        val += '\n'
        t += 1

    show = Toplevel()
    show.title('词频统计结果')
    ShowBox = Text(show, width = 30, height = 6)
    ShowBox.insert(1.0 , val)
    img = PhotoImage(file='test.png')
    ShowBox.pack()
    imgLabel = Label(show,image=img)
    imgLabel.pack()
    show.mainloop()

def count_all_words():  #统计文章总词数
    get_text()
    global words
    messagebox.showinfo('字数统计','文章总字数为:'+str(len(words)))

def show_all_words():   #展示所有单词
    if len(words) > 2000:
        messagebox.showwarning('警告', '所选文件过长，在窗口中展示将耗费大量时间，故全部单词将在Console中展示')
        for i in words:
            print(i, end = ' ')
    else:
        clean()
        main.TextBox.insert('insert',words)

def Replace():      #文本替换界面
    Replace.rp = Tk()
    Replace.rp.title('文本替换')

    allframe = Frame(Replace.rp)
    textframe = Frame(allframe)
    buttonframe = Frame(allframe)

    textframe.pack(side=LEFT)
    buttonframe.pack(side=RIGHT)

    label = Label(Replace.rp, text='请按照要求填入替换与被替换词')
    inplabel = Label(textframe, text='查找：')
    ouplabel = Label(textframe, text='替换：')
    Replace.InpEntry = Entry(buttonframe, width=20)
    Replace.OutEntry = Entry(buttonframe, width=20)
    button = Button(Replace.rp, text='全部替换', command = replace_word)

    label.pack(side=TOP)
    allframe.pack(side=TOP)
    textframe.pack(side=LEFT)
    buttonframe.pack(side=RIGHT)

    inplabel.pack(side=TOP, pady=5)
    ouplabel.pack(side=BOTTOM, pady=5)
    Replace.InpEntry.pack(side=TOP, pady=5)
    Replace.OutEntry.pack(side=BOTTOM, pady=5)
    button.pack(side=BOTTOM, pady=5)

    Replace.rp.mainloop()

def addstop():  #添加停用词
    global execludes
    addstop.add = Tk()
    addstop.add.title('停用词添加系统')
    addstop.add.AddLabel = Label(addstop.add, text='请添加停用词，如需添加多个停用词，请使用空格进行分割').pack()
    addstop.add.AddEntry = Entry(addstop.add, width=20)
    addstop.add.AddEntry.pack()
    addstop.add.AddButton = Button(addstop.add, text='添加', command = add_word).pack()
    addstop.add.mainloop()
    add_word()

def getword():
    global get_single_word
    getword.get = Tk()
    getword.get.title('单词计次系统')
    getword.get.label = Label(getword.get, text='请输入你想要查找的单词').pack()

    getword.SearchWord = Entry(getword.get, width=20)
    getword.SearchWord.pack()
    getword.SearchButton = Button(getword.get, text='确认', command=count_single_word).pack()

    getword.get.mainloop()

def count_single_word():    #查找单个单词
    global count
    search = getword.SearchWord.get()
    make_temp_dict()
    num = count.get(search, 0)
    messagebox.showinfo('结果','单词【'+str(search)+'】在文本中出现的次数为【'+str(num)+'】')
    getword.get.destroy()

def main():         #主界面
    global txt

    main.top = Tk()
    main.top.title('x帆の文本处理系统')
    main.top.protocol("WM_DELETE_WINDOW", on_closing)    #退出确认
    main.TextFrame = Frame(main.top, bg='#fffffc')  #左边栏，用于布局文本框
    main.TextFrame.pack(side=LEFT, fill=BOTH, expand=YES)

    main.TextBox = Text(main.TextFrame, width=60, height=36, background='#fffffc')
    main.TextBox.insert('insert',txt)
    main.Scroll = Scrollbar()   #拖动条

    get_text()

    ButtonFrame = Frame(main.top, bg='#fffffc')     #右边栏，用于布局按钮
    ButtonFrame.pack(side=RIGHT, fill=BOTH, expand=YES)
    #按钮部分---按照顺讯编排----#
    main.HintLabel = Label(ButtonFrame, text='功能栏', fg='#17184b', bg='#fffffc')
    main.RunButton = Button(ButtonFrame, text='词频统计',command = counts, fg='#17184b', width=12, height=2)
    main.CountAllButton = Button(ButtonFrame, text='字数统计', command = count_all_words, fg='#0f2350', width=12, height=2)
    main.ReplaceButton = Button(ButtonFrame, text='文本替换', command = Replace, fg='#223a70',width=12, height=2)
    main.HighLightButton = Button(ButtonFrame, text='添加停用词', command = addstop, fg='#274a78', width=12, height=2)
    main.ShowAllWordsButton = Button(ButtonFrame, text='展示所有单词', command = show_all_words, fg='#19448e', width=12, height=2)
    main.ProtectButton = Button(ButtonFrame, text='开启护眼模式', command = protect_mode, fg='#4c6cb3', width=12, height=2)
    main.FindButton = Button(ButtonFrame, text='统计单词个数', command = getword, fg='#1e50a2', width=12, height=2)
    main.NewButton = Button(ButtonFrame, text='打开新文件',command = New ,fg='#f8b500', width=12, height=2)
    main.CleanButton = Button(ButtonFrame, text='清空文本框', command = clean, fg='#ea5506', width=12, height=2 )
    main.QuitButton = Button(ButtonFrame, text='退出程序', command = on_closing, fg='#b7282e', width=12, height=2)

    main.Scroll.pack(side=RIGHT,fill=Y)     #打包拖动条，布局在最右侧，填充y轴
    main.Scroll.config(command=main.TextBox.yview)
    main.TextBox.config(yscrollcommand=main.Scroll.set)
    main.TextBox.pack(side=LEFT,fill=Y)

    #----布局界面-----按照从上至下分配布局-----#
    main.HintLabel.pack(side=TOP,padx=10, pady=5)
    main.RunButton.pack(side=TOP,padx = 10, pady=5)
    main.CountAllButton.pack(side=TOP,padx = 10, pady=5)
    main.ReplaceButton.pack(side=TOP,padx = 10, pady=5)
    main.HighLightButton.pack(side=TOP,padx = 10, pady=5)
    main.ShowAllWordsButton.pack(side=TOP, padx = 10, pady=5)
    main.FindButton.pack(side=TOP,padx = 10, pady=5)
    main.ProtectButton.pack(side=TOP,padx = 10, pady=5)
    main.QuitButton.pack(side=BOTTOM,padx = 10, pady=5)
    main.CleanButton.pack(side=BOTTOM,padx = 10, pady=5)
    main.NewButton.pack(side=BOTTOM,padx = 10, pady=5)
    main.top.mainloop()

def inpname():          #打开文件界面
    global name
    inpname.inp = Tk()

    inpname.inp.title('x帆の文本处理系统')
    file = Label(inpname.inp, text='添加文件：')

    inpname.file_name = Entry(inpname.inp, width = 20)

    button = Button(inpname.inp, text='确认',command = tryinp)
    getbutton = Button(inpname.inp, text='浏览', command = get_file)

    file.grid_configure(column = 1, row = 1, columnspan = 1, rowspan = 1)
    inpname.file_name.grid_configure(column = 2, row = 1, columnspan = 1, rowspan = 1)
    button.grid_configure(column = 1, row = 3, columnspan = 1, rowspan = 1)
    getbutton.grid_configure(column = 3, row = 1, columnspan = 1, rowspan = 1)

    inpname.inp.mainloop()

def tryinp():           #输入文件校验函数
    global txt
    name = inpname.file_name.get()

    if '/' not in name:
        try:
            open(str(name)+'.txt').read()
        except FileNotFoundError:
            messagebox.showerror('错误', '找不到该文件')
        else:
            txt = open(str(name)+'.txt').read()
            messagebox.showinfo('成功', '打开成功，即将进入主界面')
            inpname.inp.destroy()
            main()
    else:
        val = name.split('.')
        if val[-1] != 'txt':
            messagebox.showerror('错误', '请选择txt文件')
        else:
            try:
                open(str(name),'r').read()
            except FileNotFoundError:
                messagebox.showerror('错误', '找不到该文件')
            else:
                txt = open(str(name),'r').read()
                messagebox.showinfo('成功', '打开成功，即将进入主界面')
                inpname.inp.destroy()
                main()

inpname()
