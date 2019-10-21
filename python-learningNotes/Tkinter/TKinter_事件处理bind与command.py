import tkinter
import tkinter.messagebox
import time
def sayHello(event):
    showText = '当前的位置是：x:{:},y:{:}'.format(event.x,event.y)
    tips = tkinter.Label(root,text = showText).place(x=event.x,y=event.y)
def sayHi():
    tkinter.messagebox.showinfo('问候','Hi,every one!')
root = tkinter.Tk()
root.title('事件处理')
root.geometry('600x800+0+0')
testButton = tkinter.Button(root, text='testButton',command = sayHi)
root.bind('<Button -1>',sayHello)
testButton.pack()
root.mainloop()

# bind可以绑定组件，指定触发事件：点击，按键之类的
# command 比较单一，只能指定触发特定的函数