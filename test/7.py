import tkinter
import random


class Matrix():
    def __init__(self, side, master=None):
        self.master = master
        self.myFrame = tkinter.Frame(self.master)
        self.array = []
        self.color_array = []
        self.side = side
        for i in range(side * side):
            randomValue = str(random.randint(0, 1))
            self.array.append(int(randomValue))
            label = tkinter.Button(self.myFrame, text=randomValue, width=3, height=1,activeforeground='blue')
            label.bind('<Button-1>', self.click)
            label.grid(row=i // side, column=i % side)
        self.get_color_array()
        self.coloring()

    def get_color_array(self):
        dp = []
        for i in range(0, self.side + 2):
            set = []
            for j in range(0, self.side + 2):
                set.append(0)
            dp.append(set)
        for i in range(1, self.side + 1):
            dp[1][i] = self.array[i - 1]
        for i in range(1, self.side + 1):
            dp[i][1] = self.array[(i - 1) * self.side]
        max_s = 0
        max_x = 0
        max_y = 0
        for i in range(1, self.side + 1):
            for j in range(1, self.side + 1):
                if self.array[(i - 1) * self.side + j - 1] == 1:
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
                dp.append((i - 1) * self.side + j)
        self.color_array.clear()
        self.color_array = dp

    def coloring(self):

        for i in self.color_array:
            if i == 1:
                self.myFrame.children['!button']['background'] = 'red'
            else:
                self.myFrame.children['!button{}'.format(i)]['background'] = 'red'

    def get_array(self):
        self.array.clear()
        for i in range(1, self.side * self.side + 1):
            if i == 1:
                self.array.append(int(self.myFrame.children['!button']['text']))
            else:
                self.array.append(int(self.myFrame.children['!button{}'.format(i)]['text']))

    def reWihite(self):
        for i in range(1, self.side*self.side + 1):
            if i == 1:
                self.myFrame.children['!button']['background'] = 'white'
            else:
                self.myFrame.children['!button{}'.format(i)]['background'] = 'white'
        # 将所有颜色重置
    def click(self, event):
        event.widget['text'] = str((int(event.widget['text']) + 1) % 2)  # 数字翻转
        self.reWihite()
        self.get_array()
        self.get_color_array()
        self.coloring()


if __name__ == '__main__':
    root = tkinter.Tk()
    matrix = Matrix(10, root)
    matrix.myFrame.pack()
    root.mainloop()
