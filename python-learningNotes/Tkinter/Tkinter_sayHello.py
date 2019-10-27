import tkinter as tk
from tkinter import messagebox


def sayHello(e):
    messagebox.showinfo('来自tkinter的问候：', 'Hello Everyone!')


root = tk.Tk()  # 创建主窗口，root为TK类的一个实例
root.title('Say Hello')  # 设置窗口的标题

button = tk.Button(root, text='点我',command = sayHello)
# root:表明的归属于哪一个窗口的控件
# text:按钮要显示的文本
# command：点击按钮之后要执行的文本
button.pack()
# 将组件打包好装到窗口上
root.mainloop()
# 启动窗口消息循环
