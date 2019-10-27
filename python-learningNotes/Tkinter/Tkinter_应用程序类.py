import tkinter as tk
from tkinter import messagebox
class Application(tk.Frame):#继承自tk.Frame
    def __init__(self,master= None):
        tk.Frame.__init__(self,master)#调用父类的构造函数
        self.pack()#
        self.creatWidgets()
    def creatWidgets(self):
        self.buttonSayHi = tk.Button(self,text = 'Hello',command = self.SayHi)
        self.buttonSayHi.pack()
        self.buttonQuit = tk.Button(self,text = 'Quit',command = self.master.destroy)
        self.buttonQuit.pack()
    def SayHi(self):
        tk.messagebox.showinfo('Message','Hello Everyone!')
root = tk.Tk()
app = Application(master= root)
app.mainloop()