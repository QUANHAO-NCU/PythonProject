import tkinter
import tkinter.messagebox


def showHello():
    tkinter.messagebox.showinfo('tips','Hello world')

root = tkinter.Tk()
root.title('Button')
Button1 = tkinter.Button(root, text='Button1',command=showHello)
Button1.place(x=0, y=100)
root.mainloop()
