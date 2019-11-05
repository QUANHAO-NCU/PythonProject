import tkinter
import sqlite3
from tkinter import messagebox, font

try:  # 创建数据库
    conn = sqlite3.connect('mindGame-qh6110116148.db')  # 链接数据库
    cursor = conn.cursor()  # 打开游标
    conn.execute(
        'create table if not exists QA (id varchar(20) primary key, question varchar(40),Answer_A varchar(40),Answer_B varchar(40),Answer_C varchar(40), Answer_D varchar(40), right_Answer varchar(10))')
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (1,'哈雷慧星的平均周期为', '54年', '56年', '73年', '83年', 'C')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (2,'夜郎自大中“夜郎”指的是现在哪个地方？', '贵州', '云南', '广西', '福建', 'A')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (3,'在中国历史上是谁发明了麻药', '孙思邈', '华佗', '张仲景', '扁鹊', 'B')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (4,'京剧中花旦是指', '年轻男子', '年轻女子', '年长男子', '年长女子', 'B')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (5,'篮球比赛每队几人？', '4', '5', '6', '7', 'B')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (6,'在天愿作比翼鸟，在地愿为连理枝。讲述的是谁的爱情故事？', '焦钟卿和刘兰芝', '梁山伯与祝英台', '崔莺莺和张生', '杨贵妃和唐明皇', 'D')")
    cursor.execute(
        "insert into QA (id,question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values (7,'世界上最好的编程语言是？', 'Python', 'Java', 'C++','PHP', 'A')")
    conn.commit()
    cursor.close()
    conn.close()
except:
    pass
conn = sqlite3.connect('mindGame-qh6110116148.db')  # 链接游戏用的数据库
cursor = conn.cursor()
QAList = cursor.execute('select * from QA')
QAList = list(QAList)  # 获取问题列表
QALength = len(QAList)  # 取得问题的个数，便于判断游戏结束时间
cursor.close()
conn.close()
right_Answer = ''  # 记录正确答案
score = 0  # 玩家的得分
QuestionOrder = 0  # 问题的顺序
right_answer = {'A': 2, 'B': 3, 'C': 4, 'D': 5}


def start():
    Start_Button.destroy()
    RefreshQuestion()
    QuestionBox.pack()
    ButtonBox.pack()


def end():
    global score
    global QuestionOrder
    global right_Answer
    if (tkinter.messagebox.askyesno('提示：', '是否重新开始游戏？') == 'YES'):
        score = 0
        QuestionOrder = 0
        right_Answer = ''


def RefreshQuestion():  # 刷新问题
    global right_Answer
    global QuestionOrder
    Question["text"] = QAList[QuestionOrder][1]
    Answer_A['text'] = 'A:' + QAList[QuestionOrder][2]
    Answer_B['text'] = 'B:' + QAList[QuestionOrder][3]
    Answer_C['text'] = 'C:' + QAList[QuestionOrder][4]
    Answer_D['text'] = 'D:' + QAList[QuestionOrder][5]
    right_Answer = QAList[QuestionOrder][6]
    QuestionOrder += 1
    var.set(None)


def NextQuestion():  # 得分判断
    global score
    if (var.get() == right_Answer):
        tkinter.messagebox.showinfo('恭喜！', "恭喜你答对了！")
        score += 10
    elif (var.get() != right_Answer):
        tkinter.messagebox.showinfo('抱歉：', "抱歉，答错了")
        tkinter.messagebox.showinfo('提示:', "正确答案是：" + QAList[QuestionOrder - 1][right_answer[right_Answer]])
    else:
        tkinter.messagebox.showinfo("你没有选择任何答案！")
    if (QuestionOrder == QALength):
        tkinter.messagebox.showinfo("提示：", "题目做完了\n点击得分，查看你的得分！")
        return
    RefreshQuestion()


def ShowScore():  # 显示得分
    tkinter.messagebox.showinfo('得分：', '你的得分是：' + str(score))


root = tkinter.Tk()  # 创建主窗口，位置布置
root.title('智力问答小游戏')
root.geometry('800x456+200+100')
# 设置程序子窗口，根据要求在合适的时候放到主窗口
try:
    img_gif = tkinter.PhotoImage(file='mindGame-qh6110116148.gif')
    Start_Button = tkinter.Button(root, text='开始', font=('楷体', 64), command=start, image=img_gif,
                                  compound=tkinter.CENTER)
except:
    Start_Button = tkinter.Button(root, text='开始', font=('楷体', 64), command=start)
Start_Button.pack()  # 开始
var = tkinter.StringVar()
QuestionBox = tkinter.Frame(root)
ButtonBox = tkinter.Frame(root)
Question = tkinter.Label(QuestionBox, font=('楷体', 22), text='')
Question.pack()
Answer_A = tkinter.Radiobutton(QuestionBox, value='A', variable=var, font=('楷体', 20), text='')
Answer_A.pack()
Answer_B = tkinter.Radiobutton(QuestionBox, value='B', variable=var, font=('楷体', 20), text='')
Answer_B.pack()
Answer_C = tkinter.Radiobutton(QuestionBox, value='C', variable=var, font=('楷体', 20), text='')
Answer_C.pack()
Answer_D = tkinter.Radiobutton(QuestionBox, value='D', variable=var, font=('楷体', 20), text='')
Answer_D.pack()
Summit_Button = tkinter.Button(ButtonBox, text='下一题', font=('楷体', 20), command=NextQuestion)
Summit_Button.pack(side=tkinter.LEFT)
Score_Button = tkinter.Button(ButtonBox, text='得分', font=('楷体', 20), command=ShowScore)
Score_Button.pack(side=tkinter.RIGHT)
root.mainloop()
