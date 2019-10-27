import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.title("窗口布局测试")
# 设置窗口的标题

root.geometry('800x600+0+0')
# 设置窗口的大小，参数为 宽 x 高 ± x ± y
# +x表示主窗口左边离屏幕左边的距离，-x表示主窗口右边离屏幕右边的距离
# +y表示主窗口上边离屏幕上边的距离，-y表示主窗口下边离屏幕下边的距离
tkinter.Label(root,text='用户名',width=6).place(x=1,y=1)
tkinter.Entry(root,width=20).place(x=40,y=1)
tkinter.Label(root,text='密码',width=6).place(x=1,y=22)
tkinter.Entry(root,width=20).place(x=40,y=22)
tkinter.Button(root,text='登录',width=8).place(x=50,y=45)
tkinter.Button(root,text='取消',width=8).place(x=110,y=45)
root.mainloop()

# place设想在主窗口构建一个坐标系，用坐标精确安排控件的位置
# 缺点，控件的位置和大小不会随着主窗口的放大和缩小而自适应变化