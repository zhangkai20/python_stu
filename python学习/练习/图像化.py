#! /usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk


def closewindow():
    #   设置提示信息
    messagebox.showerror(title='错误',message='不能关闭')
    return
def guanbi():
    #   关闭窗口
    window.destroy()
def shi():
    #   创建一个顶级窗口，依赖原始窗口存在
    shi = Toplevel(window)
    shi.title('太好了')
    shi.geometry('250x100+550+300')
    shi.protocol('WM_DELETE_WINDOW',closewindow)
    lable = Label(shi, text='你终于承认了', font=("微软雅黑", 20))
    lable.pack()
    botten = Button(shi, text='是的', width=7, height=3, command=guanbi)
    botten.pack()
    shi.mainloop()
def bushi():
    bushi = Toplevel(window)
    bushi.title('你确定？')
    bushi.geometry('250x90+550+300')
    bushi.protocol('WM_DELETE_WINDOW',closewindow)
    lable = Label(bushi, text='好好想想', font=("微软雅黑", 20))
    lable.pack()
    botten = Button(bushi, text='好的', width=7, height=3, command=bushi.destroy)
    botten.pack()
    bushi.mainloop()
#   创建一个窗口
window = Tk()
#   命名窗口的标题
window.title('hellow!')
#   设置窗口大小,设置窗口位置   +前面为窗口大小
window.geometry('400x500+500+200')
#   当用户关闭窗口时触发
window.protocol('WM_DELETE_WINDOW',closewindow)
#   添加文本标签(控件)
lable = Label(window,text='hellow!',font=("楷体",20))
#   显示标签
lable.grid(row=0,column=0,sticky=W)
#   添加图片控件
# imag = PhotoImage(file='cc.png')
# image = Label(window,image=imag)
# image.grid(row=2,columnspan=2)
photo = Image.open('6.jpg')
phot = ImageTk.PhotoImage(photo)
pho = Label(window,image=phot)
#   显示数据
pho.grid(row=1,columnspan=1)
#   添加一个按钮控件
botten = Button(window,text='是的',width=10,height=3,command=shi)
botten.grid(row=2,column=0,sticky=W)
botten = Button(window,text='不是',width=5,height=2,command=bushi)
botten.grid(row=2,column=0,sticky=E)
#   显示窗口
window.mainloop()