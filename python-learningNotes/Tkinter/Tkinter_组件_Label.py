import tkinter
from tkinter import messagebox
def sayHello():
    tkinter.messagebox.askyesno('欢迎','Hello,every one')
def tips(event):
    tkinter.messagebox.askyesnocancel('程序说明如下：')
root = tkinter.Tk()
root.title('Tkinter 组件：Label')
Label1 = tkinter.Label(root, text='姓名：')
Label1.config(width=20,bg='pink',fg='blue')#标签的填充内容
Label1['anchor']='center'#标签的内容的排版方式
Label1.place(x=1,y=1)

LabelFrame = tkinter.LabelFrame(root,text='标签组',width=200,height=120,bg='blue',fg='pink')
LabelFrame.place(x=100,y=100)
button1 = tkinter.Button(LabelFrame,text='欢迎',command=sayHello).pack(side='left')
button2 = tkinter.Button(LabelFrame,text='说明')
button2.bind('<Button -1>',tips)
button2.pack(side='left')
root.mainloop()
