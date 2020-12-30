import os
from PIL import Image                   #图片转换模块
import tkinter                                  #界面
import tkinter.filedialog                   #文件/文件夹的选择
import tkinter.messagebox             #警告

class window:
    def __init__(self):
        self.root=root=tkinter.Tk()
        self.root.title('图片格式转换大师')
        label = tkinter.Label(root, text='图片格式转换大师',font=99)
        label.place(x=125, y=10)
        label=tkinter.Label(root,text='选择文件')
        label.place(x=5,y=200)
        label = tkinter.Label(root, text='保存地址')
        label.place(x=5, y=240)
        self.entry1=tkinter.Entry(root)                                              #图片选择输入框
        self.entry1.place(x=60,y=200)
        self.entry2 = tkinter.Entry(root)                                             # 图片保存输入框
        self.entry2.place(x=60, y=240)
        self.buttonbrowser1=tkinter.Button(root,text='浏览',            #按钮，功能键，绑定浏览文件框，用选择图片路径
                                          command=self.browser)
        self.buttonbrowser1.place(x=210,y=197)
        self.buttonbrowser2 = tkinter.Button(root, text='浏览',         # 按钮，功能键，绑定浏览文件框，用以选择图片的保存路径
                                            command=self.savepath)
        self.buttonbrowser2.place(x=210, y=237)
        framef=tkinter.Frame(root)
        framef.place(x=5,y=45)
        framet=tkinter.Frame(root)
        framet.place(x=100,y=45)
        self.fimage=tkinter.StringVar()                                             #输入变量
        self.timage=tkinter.StringVar()                                             #输入变量
        self.status = tkinter.StringVar()                                            #输入变量
        self.fimage.set('.bmp')
        self.timage.set('.bmp')
        labelfrom=tkinter.Label(framef,text='From')                         #Label标签，说明，图片原格式
        labelfrom.pack(anchor='w')
        labelto = tkinter.Label(framet, text='to')                                 #Label标签，说明，要转换成的图片格式
        labelto.pack(anchor='w')
        frbmp=tkinter.Radiobutton(framef,variable=self.fimage,       #Radiobutton单选按钮
                                  value='.bmp',text='BMP')
        frbmp.pack(anchor='w')
        frjpg = tkinter.Radiobutton(framef, variable=self.fimage,      #Radiobutton单选按钮
                                    value='.jpg', text='JPG')
        frjpg.pack(anchor='w')
        frgif = tkinter.Radiobutton(framef, variable=self.fimage,        #Radiobutton单选按钮
                                    value='.gif', text='GIF')
        frgif.pack(anchor='w')
        frpng = tkinter.Radiobutton(framef, variable=self.fimage,      #Radiobutton单选按钮
                                    value='.png', text='PNG')
        frpng.pack(anchor='w')
        trbmp = tkinter.Radiobutton(framet, variable=self.timage,      #Radiobutton单选按钮
                                    value='.bmp', text='BMP')
        trbmp.pack(anchor='w')
        trjpg = tkinter.Radiobutton(framet, variable=self.timage,         #Radiobutton单选按钮
                                    value='.jpg', text='JPG')
        trjpg.pack(anchor='w')
        trgif = tkinter.Radiobutton(framet, variable=self.timage,          #Radiobutton单选按钮
                                    value='.gif', text='GIF')
        trgif.pack(anchor='w')
        trpng = tkinter.Radiobutton(framet, variable=self.timage,        #Radiobutton单选按钮
                                    value='.png', text='PNG')
        trpng.pack(anchor='w')
        self.buttonconv=tkinter.Button(root,text='开始转换',                #按钮，功能键，绑定转换方法
                                       command=self.conv)
        self.buttonconv.place(x=250,y=70)
        self.labelstatus = tkinter.Label(root, textvariable=self.status)  # 标签内容可变，显示转换结果
        self.labelstatus.place(x=238, y=125)
    def mainloop(self):                                                                       #主屏幕运行框，设置最大最小尺寸
        self.root.minsize(380,380)
        self.root.maxsize(380, 380)
        self.root.mainloop()
    def browser(self):                                                                         #浏览框
        directory=tkinter.filedialog.askopenfilenames(title='图片格式转换') #直接获取文件路径传给文本框时格式发生变化不好处理，
        with open('imgspath.txt','w+') as f:                                           #所以将获得路径写入txt文档以便处理
            for dir in directory:
                f.write(dir)
                f.write('\n')
        if directory:                                                                              #将图片路径在文本框中显示
            self.entry1.delete(0,tkinter.END)
            self.entry1.insert(tkinter.END,directory)
    def savepath(self):
        savepath = tkinter.filedialog.askdirectory(title='图片格式转换') #将文件路径在文本框中显示
        if savepath:
            self.entry2.delete(0,tkinter.END)
            self.entry2.insert(tkinter.END,savepath)
    def conv(self):                                                                             #转换函数
        n=0
        ff= self.fimage.get()                                                                 # .jpg
        t=self.timage.get()                                                                   #.bmp 获取用户选择的转换格式
        path=self.entry1.get()
        save_path = self.entry2.get()
        n=0
        if path=='':                                                                                #若未选择路径发出警告信息
            tkinter.messagebox.showerror('Python tkinter','请选择图片路径')
            return
        if save_path=='':
            tkinter.messagebox.showerror('Python tkinter','请选择保存路径')
            return
        with open('1.txt', 'r') as f:                                                          #读取图片路径信息
            files = f.readlines()
            for file in files:
                file1=file.replace('\n','')                                                      #初始文件绝对路径
                file2=file.replace('\n','').split('/')[-1]                                     #文件名
                file3=file2.split('.')[0]                                                          #除去后缀
                file4=save_path+'/'+file3+t                                                #新的文件绝对路径
                Image.open(file1).save(file4)
                n+=1
        self.status.set('成功转换%d张照片' % n)

window=window()
window.mainloop()
