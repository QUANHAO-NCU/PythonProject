import tkinter
import random
import time
from tkinter import messagebox

# import tensorflow as tf
####################################################################
poker_list = [['黑桃', '1'], ['红桃', '1'], ['梅花', '1'], ['方块', '1'], ['黑桃', '2'], ['红桃', '2'], ['梅花', '2'], ['方块', '2'],
              ['黑桃', '3'], ['红桃', '3'], ['梅花', '3'], ['方块', '3'], ['黑桃', '4'], ['红桃', '4'], ['梅花', '4'], ['方块', '4'],
              ['黑桃', '5'], ['红桃', '5'], ['梅花', '5'], ['方块', '5'], ['黑桃', '6'], ['红桃', '6'], ['梅花', '6'], ['方块', '6'],
              ['黑桃', '7'], ['红桃', '7'], ['梅花', '7'], ['方块', '7'], ['黑桃', '8'], ['红桃', '8'], ['梅花', '8'], ['方块', '8'],
              ['黑桃', '9'], ['红桃', '9'], ['梅花', '9'], ['方块', '9'], ['黑桃', '10'], ['红桃', '10'], ['梅花', '10'],
              ['方块', '10'],
              ['黑桃', 'J'], ['红桃', 'J'], ['梅花', 'J'], ['方块', 'J'], ['黑桃', 'Q'], ['红桃', 'Q'], ['梅花', 'Q'], ['方块', 'Q'],
              ['黑桃', 'K'], ['红桃', 'K'], ['梅花', 'K'], ['方块', 'K']]
tran_dit = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


####################################################################构造robot，对象，player为robot的继承
class robot(object):
    points = 0  # 点数
    win_num = 0  # 获胜次数
    fail_num = 0  # 失败次数
    card_list = []  # 已获得的卡牌列表
    score = 0  # 当前卡牌的分值
    is_get_card = 1  # 状态，是否接着拿牌
    card_list_pic = []  # 此列表用于存放玩家当前扑克牌对应的图片

    def __init__(self, points):
        self.points = points
        self.card_list = []  # 已获得的卡牌列表
        self.score = 0  # 当前卡牌的分值
        self.is_get_card = 1  # 状态，是否接着拿牌

    def cal_card_score(self):
        self.score = 0
        for i in self.card_list:
            self.score += tran_dit[i[1]]
        self._is_get_card()
        return self.score

    def _is_get_card(self):
        if self.score < 21:
            self.is_get_card = 1
        else:
            self.is_get_card = 0
        return self.is_get_card
        '''
        后期可以根据已有的牌，场上剩余的牌数等信息，加入神经网络进行只能判断是否要牌
        '''

    def get_card(self, poker_list_playing):
        self.card_list.append(hand_out_card(poker_list_playing))
        self.cal_card_score()

    def dont_get(self):
        self.is_get_card = 0

    def show_my_card(self, flag):
        global player_card_list
        global Robot_card_list
        j = 0
        if (flag == 'pU'):
            for i in self.card_list:
                card_pic = tkinter.PhotoImage(
                    file='poker_pic/' + i[0] + ' ' + i[1] + '.gif')  # 生成tkinter的图片类型
                player_card_list[j].config(image=card_pic)
                player_card_list[j].image = card_pic
                player_card_list[j].place(x=50 + j * 135, y=140)
                j = j + 1
        elif (flag == 'rD'):
            for i in self.card_list:
                card_pic = tkinter.PhotoImage(
                    file='poker_pic/背面.gif')  # 生成tkinter的图片类型
                Robot_card_list[j].config(image=card_pic)
                Robot_card_list[j].image = card_pic
                Robot_card_list[j].place(x=650 + j * 130, y=5)
                j = j + 1
        elif (flag == 'rU'):
            for i in self.card_list:
                card_pic = tkinter.PhotoImage(
                    file='poker_pic/' + i[0] + ' ' + i[1] + '.gif')  # 生成tkinter的图片类型
                Robot_card_list[j].config(image=card_pic)
                Robot_card_list[j].image = card_pic
                Robot_card_list[j].place(x=650 + j * 130, y=5)
                j = j + 1


class player(robot):
    pass  # 继承于robot


####################################################################
def hand_out_card(poker_list_playing):
    end = len(poker_list_playing) - 1
    random_position = random.randint(0, end)
    get_card = poker_list_playing[random_position]
    poker_list_playing.pop(random_position)
    poker_num['text'] = '当前牌堆剩余：%d' % len(poker_list_playing)
    return get_card


def game_init(rpoints, ppoints):
    global poker_list_playing
    global player_card_list
    global Robot_card_list
    poker_list_playing = poker_list.copy()
    invite.pack_forget()
    for i in player_card_list:
        i.place_forget()
    for i in Robot_card_list:
        i.place_forget()
    r1.__init__(rpoints)
    p1.__init__(ppoints)
    robot_chat['text'] = '：年轻人，赌狗赌到最后一无所有！放弃吧'
    game_start()


def game_ready():
    Welcome.pack_forget()
    Tips.place_forget()
    Star_Button.place_forget()
    p_poker.place_forget()
    game_init(500, 500)
    Robot_Frame.pack()
    Program_Frame.pack()
    Player_Frame.pack()


def game_start():
    global poker_list_playing
    r1.get_card(poker_list_playing)
    r1.get_card(poker_list_playing)
    r1.show_my_card('rD')
    p1.get_card(poker_list_playing)
    p1.get_card(poker_list_playing)
    p1.show_my_card('pU')


def player_get_card():
    global poker_list_playing
    if (not (r1.is_get_card or p1.is_get_card)):
        game_judge()
        return  # 唯一退出条件，player和robot都不再要牌
    if (p1.is_get_card):
        p1.get_card(poker_list_playing)
        p1.show_my_card('pU')
        if (p1.score > 21):
            p1.dont_get()
            game_judge()  # 点数过高，自动爆
            return
    robot_get_card()


def robot_get_card():
    global poker_list_playing
    if (r1.is_get_card):
        robot_chat['text'] = '：我再要一张牌嘿嘿'
        time.sleep(0.2)
        r1.get_card(poker_list_playing)
        r1.show_my_card('rD')
        if (r1.score >= 19):
            r1.dont_get()  # robot在当前点数大于19后不再要牌
        elif (r1.score > 21):
            game_judge()  # 点数过高，爆了，这一回合结束
            return


def game_controller():
    p1.dont_get()
    while (r1.is_get_card or p1.is_get_card):
        player_get_card()
    game_judge()


def game_judge():
    if (r1.score > 21 or (p1.score <= 21 and p1.score > r1.score)):
        tkinter.messagebox.showinfo('恭喜', '你赢了！')
        p1.win_num += 1
        r1.fail_num += 1
        p1.points += 100
        r1.points -= 100
        r1.show_my_card('rU')
        robot_chat['text'] = '：卧槽，无情！这次算我运气不好！'
    elif (p1.score > 21 or (p1.score < r1.score and r1.score <= 21)):
        tkinter.messagebox.showinfo('emmmmmm', '似乎电脑玩家的运气更好')
        p1.fail_num += 1
        r1.win_num += 1
        r1.points += 100
        p1.points -= 100
        r1.show_my_card('rU')
        robot_chat['text'] = '：年轻人，赌狗赌到最后一无所有！放弃吧'
    elif (p1.score == r1.score):
        tkinter.messagebox.showinfo('也许这就是缘分吧', '巧了，你的点数和电脑玩家的一样！')
        r1.show_my_card('rU')
        robot_chat['text'] = '：Emmmmmmmm………………'
    robot_information['text'] = ('剩余点数：{0: >4}，已胜利：{1: >2}局，已失败：{2: >3}局'.format(r1.points, r1.win_num,
                                                                                 r1.fail_num))
    player_information['text'] = ('剩余点数：{0: >4}，已胜利：{1: >2}局，已失败：{2: >3}局'.format(p1.points, p1.win_num,
                                                                                  p1.fail_num))

    if (tkinter.messagebox.askyesno('一份哲学的邀请：', '那么，继续吗？')):
        # tkinter只能在当前函数运行结束之后才刷新窗口，这是不得已而为之的提示框
        ready_re_game()
    else:
        root.destroy()


def ready_re_game():
    time.sleep(2)
    Robot_Frame.pack_forget()
    Program_Frame.pack_forget()
    Player_Frame.pack_forget()
    invite.pack()


def re_game():
    Robot_Frame.pack()
    Program_Frame.pack()
    Player_Frame.pack()
    game_init(r1.points, p1.points)


if __name__ == '__main__':
    root = tkinter.Tk()
    root.geometry('1366x768+0+0')
    root.title('21点游戏')
    root.propagate(0)
    r1 = robot(500)  # 电脑玩家对象
    p1 = player(500)  # 玩家对象
    poker_list_playing = poker_list.copy()  # 用于游戏的牌堆
    ####################################################################欢迎界面区
    Welcome = tkinter.Label(root, text='年轻人，你VAN过黑杰克吗♂', font=('楷体', 32))
    Welcome.pack()
    p_poker_pic = tkinter.PhotoImage(file='icon_pic/哲学扑克.gif')
    p_poker = tkinter.Label(root, image=p_poker_pic)
    p_poker.place(x=431, y=150)
    Star_Button = tkinter.Button(root, text='开始VAN', font=('楷体', 28), command=game_ready)
    Star_Button.place(x=594, y=550)
    Tips = tkinter.Label(root, text='Created By QH,2019-All Right Reserved!', font=('楷体', 16))
    Tips.place(x=500, y=720)
    ####################################################################电脑玩家的窗口控件区
    Robot_Frame = tkinter.Frame(root, bg='green', width=1366, height=200)
    Robot_Frame.propagate(0)  # 建立电脑玩家的子窗口
    robot_icon_pic = tkinter.PhotoImage(file='icon_pic/哲学男.gif')  # 头像图片
    robot_icon = tkinter.Label(Robot_Frame, width=132, height=120, image=robot_icon_pic)
    robot_name = tkinter.Label(Robot_Frame, text='电脑玩家-无情的要牌机器', font=('微软雅黑', 14), width=20)
    robot_information = tkinter.Label(Robot_Frame, font=('微软雅黑', 14),
                                      text='剩余点数：{0: >4}，已胜利：{1: >2}局，已失败：{2: >3}局'.format(r1.points, r1.win_num,
                                                                                           r1.fail_num))
    robot_chat = tkinter.Label(Robot_Frame, text='：' + '年轻人，赌狗赌到最后一无所有，放弃吧', font=('楷体', 18))
    Robot_card1 = tkinter.Label(Robot_Frame, image=None)
    Robot_card2 = tkinter.Label(Robot_Frame, image=None)
    Robot_card3 = tkinter.Label(Robot_Frame, image=None)
    Robot_card4 = tkinter.Label(Robot_Frame, image=None)
    Robot_card5 = tkinter.Label(Robot_Frame, image=None)
    Robot_card6 = tkinter.Label(Robot_Frame, image=None)
    Robot_card_list = [Robot_card1, Robot_card2, Robot_card3, Robot_card4, Robot_card5,
                       Robot_card6]  # 显示控件列表，用于与要显示的图片一一对应
    # ~~~
    robot_icon.place(x=5, y=32)
    robot_name.place(x=146, y=32)
    robot_information.place(x=146, y=60)
    robot_chat.place(x=146, y=126)
    # ~~~
    ####################################################################中央程序发牌区
    Program_Frame = tkinter.Frame(root, bg='yellow', width=1366, height=200)
    Program_Frame.propagate(0)  # 建立程序发牌子窗口
    poker_back_pic = tkinter.PhotoImage(file='poker_pic/背面.gif')
    poker_back = tkinter.Label(Program_Frame, image=poker_back_pic)
    pb1 = tkinter.Label(Program_Frame, image=poker_back_pic)
    pb2 = tkinter.Label(Program_Frame, image=poker_back_pic)
    poker_num = tkinter.Label(Program_Frame, font=('微软雅黑', 24), text='当前牌堆剩余：%d' % len(poker_list_playing))
    # ~~~
    poker_back.pack()
    pb1.place(x=550, y=0)
    pb2.place(x=470, y=0)
    poker_num.place(x=900, y=150)
    # ~~~
    ####################################################################玩家界面区
    Player_Frame = tkinter.Frame(root, bg='blue', width=1366, height=366)
    Player_Frame.propagate(0)  # 建立玩家子窗口
    player_icon_pic = tkinter.PhotoImage(file='icon_pic/鹦鹉兄弟.gif')
    player_icon = tkinter.Label(Player_Frame, image=player_icon_pic)
    player_name = tkinter.Label(Player_Frame, text='玩家-一个电脑狂什么狂', font=('微软雅黑', 14), width=20)
    player_information = tkinter.Label(Player_Frame, font=('微软雅黑', 14),
                                       text='剩余点数：{0: >4}，已胜利：{1: >2}局，已失败：{2: >3}局'.format(p1.points,
                                                                                            p1.win_num,
                                                                                            p1.fail_num))
    player_tips = tkinter.Label(Player_Frame, text='我抽到的牌', font=('微软雅黑', 18), width=25, height=2)
    player_Button_get_card = tkinter.Button(Player_Frame, font=('微软雅黑', 24), text='再要一张', borderwidth=0,
                                            command=player_get_card)
    player_Button_dont_get = tkinter.Button(Player_Frame, font=('微软雅黑', 24), text='不要了', borderwidth=0,
                                            command=game_controller)
    player_card1 = tkinter.Label(Player_Frame, image=None)
    player_card2 = tkinter.Label(Player_Frame, image=None)
    player_card3 = tkinter.Label(Player_Frame, image=None)
    player_card4 = tkinter.Label(Player_Frame, image=None)
    player_card5 = tkinter.Label(Player_Frame, image=None)
    player_card6 = tkinter.Label(Player_Frame, image=None)
    player_card_list = [player_card1, player_card2, player_card3, player_card4, player_card5,
                        player_card6]  # 显示控件列表，用于与要显示的图片一一对应
    # ~~~
    player_icon.place(x=5, y=2)
    player_name.place(x=146, y=2)
    player_information.place(x=146, y=30)
    player_tips.place(x=146, y=60)
    player_Button_get_card.place(x=600, y=0)
    player_Button_dont_get.place(x=600, y=68)
    # ~~~
    ####################################################################哲♂学邀请区
    invite = tkinter.Frame(root, bg='red', width=500, height=420)
    invite.propagate(0)
    invite_pic = tkinter.PhotoImage(file='icon_pic/哲学邀请.gif')
    invite_ = tkinter.Label(invite, image=invite_pic)
    invite__ = tkinter.Label(invite, text='再来一局？', font=('微软雅黑', 18))
    Button_continue = tkinter.Button(invite, font=('微软雅黑', 18), text='那就再来一局', command=re_game)
    Button_quit = tkinter.Button(invite, font=('微软雅黑', 18), text='不了，嘻嘻', command=root.destroy)
    invite_.pack()
    invite__.pack()
    Button_continue.place(x=0, y=360)
    Button_quit.place(x=357, y=360)
    ####################################################################
    root.mainloop()
