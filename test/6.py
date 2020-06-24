# import tkinter
# import random

# array = []  # 所有数
# side = 10  # 矩阵的边数
# color = []  # 要上色的矩阵


# def creatMatrix(self, side):
#     for i in range(side * side):
#         randomValue = str(random.randint(0, 1))
#         self.array.append(int(randomValue))
#         label = tkinter.Button(self.frame, text=randomValue, width=1, height=1)
#         label.bind('<Button-1>', self.clickTraver)
#         label.grid(row=i // side, column=i % side)
#
# def getcolor(frame):
#     array = []
#     for i in range(side):
#         array.append(int(frame.children['!button{}'.format(i)]['text']))
#     '''
#     你的函数名称为getIndex(self),结果保存在self.color中
#     '''
# def clickTraver(event):
#     event.widget['text'] = str((int(event.widget['text']) + 1) % 2)
#     getcolor()
#
#     self.getIndex()
#     for i in self.color:
#         self.children['!button{}'.format(i)]['background'] = 'red'
#
#
# def getIndex(self, array, side):  # array是数组，side是边长
#     self.color = []  # 每次都要置空
#     self.color = [72, 73, 82, 83]
#     # self.color = result# result 是结果数组，这个函数不用返回
#     pass
#
#
# __init__(self, Frame)
# if __name__ == '__main__':
#     root = tkinter.Tk()
#     Matrix = tkinter.Frame(root)
#     Matrix = Application(Matrix)
#     Matrix.pack()
#     root.mainloop()
import tkinter
import random

array = []  # 所有数
side = 10  # 矩阵的边数
color = []  # 要上色的矩阵


def getarray():
    global frame
    array = []
    for i in range(1,side+1):
        if i==1:
            array.append(int(frame.children['!button']['text']))
        else:
            array.append(int(frame.children['!button{}'.format(i)]['text']))
    return array


def getIndex(array, side):
    dp = []
    for i in range(0, side + 1):
        for j in range(0, side + 1):
            dp[i][j] = 0
    for i in range(1, side + 1):
        dp[1][i] = array[i - 1]
    for i in range(1, side + 1):
        dp[i][1] = array[(i - 1) * side]
    max_s = 0
    max_x = 0
    max_y = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if array[(i - 1) * side + j - 1] == 1:
                a = dp[i - 1][j - 1]
                b = dp[i - 1][j]
                c = dp[i][j - 1]
                if dp[i][j] < min(a, b, c) + 1:
                    dp[i][j] = min(a, b, c) + 1
            if dp[i][j] > max_s:
                max_x = i;
                max_y = j;
                max_s = dp[i][j]
    dp = []
    for i in range(max_x - max_s + 1, max_x + 1):
        for j in range(max_y - max_s + 1, max_y + 1):
            dp.append((i - 1) * side + j)
    return dp


def clickTraver(event):
    global side
    global frame
    event.widget['text'] = str((int(event.widget['text']) + 1) % 2)  # 数字翻转
    a = getarray()
    needcolor = getIndex(a, side)
    for i in needcolor:
        if i==1:
            frame.children['!button{}'.format(i)]['background'] = 'red'
        else:
            frame.children['!button{}'.format(i)]['background'] = 'red'
def tocolor(needcolor):
    for i in needcolor:
        if i==1:
            frame.children['!button{}'.format(i)]['background'] = 'red'
        else:
            frame.children['!button{}'.format(i)]['background'] = 'red'


def creatMatrix(side, frame):
    global array
    for i in range(side * side):
        randomValue = str(random.randint(0, 1))
        array.append(int(randomValue))
        label = tkinter.Button(frame, text=randomValue, width=1, height=1)
        label.bind('<Button-1>', clickTraver)
        label.grid(row=i // side, column=i % side)
    a = getarray()
    color = getIndex(a,side)
    tocolor(color)

if __name__ == '__main__':
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    creatMatrix(10, frame)
    frame.pack()
    root.mainloop()
