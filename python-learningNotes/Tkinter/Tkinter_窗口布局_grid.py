import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.title("窗口布局测试")
# 设置窗口的标题

root.geometry('800x600+0+0')
# 设置窗口的大小，参数为 宽 x 高 ± x ± y
# +x表示主窗口左边离屏幕左边的距离，-x表示主窗口右边离屏幕右边的距离
# +y表示主窗口上边离屏幕上边的距离，-y表示主窗口下边离屏幕下边的距离
tkinter.Label(root, text='用户名').grid(row=0, column=0)
tkinter.Entry(root).grid(row=0, column=1, columnspan=2)
tkinter.Label(root, text='密码').grid(row=1, column=0)
tkinter.Entry(root).grid(row=1, column=1, columnspan=2)
tkinter.Button(root, text='登录').grid(row=2, column=1, sticky='E')
tkinter.Button(root, text='取消').grid(row=2, column=2, sticky='W')
root.mainloop()
# grid 将整个窗口看作一个表格来安排控件的位置
