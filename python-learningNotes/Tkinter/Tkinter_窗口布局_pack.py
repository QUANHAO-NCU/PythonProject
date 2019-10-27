import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.title("窗口布局测试")
# 设置窗口的标题

root.geometry('800x600+0+0')
# 设置窗口的大小，参数为 宽 x 高 ± x ± y
# +x表示主窗口左边离屏幕左边的距离，-x表示主窗口右边离屏幕右边的距离
# +y表示主窗口上边离屏幕上边的距离，-y表示主窗口下边离屏幕下边的距离

f1 = tkinter.Frame(root)
f1.pack()
f2 = tkinter.Frame(root)
f2.pack()
f3 = tkinter.Frame(root)
f3.pack()
# 创建三个子框架

tkinter.Label(f1, text='用户名', width=15, height=5).pack(side='left', padx=0, pady=0, anchor='nw')
tkinter.Entry(f1).pack(side='right', anchor='nw')
tkinter.Label(f2, text='密码', width=15, height=5).pack(side='left', padx=0, pady=0, anchor='nw')
tkinter.Entry(f2).pack(side='right', anchor='nw')
# 创建用户名和密码的文本输入框

tkinter.Button(f3, text='登录').pack(side='left', padx=0, pady=0, anchor='nw')
tkinter.Button(f3, text='取消').pack(side='right', padx=0, pady=0, anchor='nw')
root.mainloop()

# pack 安排控件的方式像前端的div容器
