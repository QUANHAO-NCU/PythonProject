from tkinter import *


class App():
    def __init__(self, master):
        self.master = master
        self.initWidgets()
        self.expr = None

    def initWidgets(self):
        self.show = Label()
        self.show.pack()
        p = Frame(self.master)
        p.pack()
        names = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.', '=','x')
        for i in range(len(names)):
            b = Button(p, text=names[i])
            b.grid(row=i // 4, column=i % 4)
            if i != (len(names) - 1):
                b.bind('<Button-1>', self.click)
            else:
                b.bind('<Double-1>', self.doubleclick)

    def click(self, event):
        if (event.widget['text'] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')):
            self.show['text'] += event.widget['text']
            self.expr = self.show['text']
        elif (event.widget['text'] in ('+', '-', '*', '/')):
            if self.expr == None:
                self.show['text'] = "error,please input the number first"
            else:
                self.show['text'] = self.show['text'] + event.widget['text']
            # self.expr=self.expr+event.widget['text']
        elif (event.widget['text'] == '='):
            self.show['text'] = "%f" % (eval(self.expr))
            result = eval(self.expr)
            print(result)

    def doubleclick(self, event):
        self.expr = None
        self.show['text'] = ''


root = Tk()
root.title('计算器')
App(root)
root.mainloop()
