+62 # 百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8
import hashlib
import urllib
from urllib import request
import random
import json
import tkinter
import tkinter.messagebox

to_ascii = {'自动检测': 'auto', '中文': 'zh', '英语': 'en', '粤语': 'yue', '文言文': 'wyw', '日语': 'jp', '韩语': 'kor', '法语': 'fra',
            '西班牙语': 'spa',
            '泰语': 'th', '阿拉伯语': 'ara', '俄语': 'ru', '葡萄牙语': 'pt', '德语': 'de', '意大利语': 'it', '希腊语': 'el', '荷兰语': 'nl',
            '波兰语': 'pl',
            '保加利亚语': 'bul', '爱沙尼亚语': 'est', '丹麦语': 'dan', '芬兰语': 'fin', '捷克语': 'cs', '罗马尼亚语': 'rom', '斯洛文尼亚语': 'slo',
            '瑞典语': 'swe', '匈牙利语': 'hu', '繁体中文': 'cht', '越南语': 'vie'}
to_zh = {'auto': '自动检测', 'zh': '中文', 'en': '英语', 'yue': '粤语', 'wyw': '文言文', 'jp': '日语', 'kor': '韩语', 'fra': '法语',
         'spa': '西班牙语', 'th': '泰语', 'ara': '阿拉伯语', 'ru': '俄语', 'pt': '葡萄牙语', 'de': '德语', 'it': '意大利语', 'el': '希腊语',
         'nl': '荷兰语',
         'pl': '波兰语', 'bul': '保加利亚语', 'est': '爱沙尼亚语', 'dan': '丹麦语', 'fin': '芬兰语', 'cs': '捷克语', 'rom': '罗马尼亚语',
         'slo': '斯洛文尼亚语',
         'swe': '瑞典语', 'hu': '匈牙利语', 'cht': '繁体中文', 'vie': '越南语'}


def translator(source_text):
    user_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    appid = '20191106000353409'
    secretKey = 'N0KL1i38btDVTQXoYgnB'
    myurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    fromLang = source_text['from']  # 原文语种
    toLang = source_text['to']  # 译文语种
    salt = random.randint(32768, 65536)
    text = source_text['trans_result'][0]['src']  # 要翻译的文本
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()  # 信息加密
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        text) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    try:
        response = urllib.request.urlopen(myurl)
        if (response.getcode() != 200):
            tkinter.messagebox.showerror('网络错误', '您的网络未连接，无法正确使用该软件，程序结束')
            root.destroy()
            quit(0)#未联网则程序结束
        result = response.read().decode('utf-8')
        result = json.loads(result)
        return result
    except Exception as e:
        print(e)  # 在控制台输出错误信息


def get_FromLang():
    return var_FromLang.get()


def get_ToLang():
    return var_ToLang.get()


def get_src_text():
    return var_src_text.get()


def get_trans_text():
    return var_trans_text.get()


def clear_src_text(event):
    return var_src_text.set('')


def clear_trans_text(event):
    return var_trans_text.set(' ')


def History_show(new_record):
    new_text = '源文语种:' + to_zh[new_record[0]] + '   ' + '源文:' + '    ' + new_record[2] + '    ' + '译文语种:' + to_zh[
        new_record[1]] \
               + '  ' + '译文:' + '    ' + new_record[3]
    History['5'] = History['4']
    History['4'] = History['3']
    History['3'] = History['2']
    History['2'] = History['1']
    History['1'] = new_text
    print(type(record[1][0]))
    for i in History:
        if (History[i] == ''):  # 消息为空的卸载组件
            record[int(i)][0].place_forget()
        if (History[i] != ''):  # 消息非空的安装组件
            record[int(i)][0].place(x=0, y=record[int(i)][1])
            record[int(i)][2].set(History[i])


def mainMenu():
    LangChoice.pack()
    Content_Box.pack()
    History_Box.pack()


def Start():
    Welcome.destroy()
    Tips.destroy()
    Star_Button.destroy()
    mainMenu()


def Click_Trans():
    src_text['from'] = to_ascii[get_FromLang()]
    src_text['to'] = to_ascii[get_ToLang()]
    src_text['trans_result'][0]['src'] = var_src_text.get()
    result = translator(src_text)
    print(result)
    var_trans_text.set(result['trans_result'][0]['dst'])
    history = []
    history.append(result['from'])
    history.append(result['to'])
    history.append(result['trans_result'][0]['src'])
    history.append(result['trans_result'][0]['dst'])
    History_show(history)


if __name__ == '__main__':
    src_text = {'from': 'en', 'to': 'zh', 'trans_result': [{'src': '', 'dst': ''}]}  # 源文本信息
    History = {'1': '', '2': '', '3': '', '4': '', '5': ''}
    root = tkinter.Tk()
    # 控件列表
    root.geometry('900x500+200+100')
    Welcome = tkinter.Label(root, text='欢迎使用百度翻译（山寨版）', font=('楷体', 32))
    Tips = tkinter.Label(root, text='Created By QH,2019-All Right Reserved!', font=('楷体', 16))
    Welcome.pack()
    Tips.place(x=259, y=460)
    Star_Button = tkinter.Button(root, text='开始使用', font=('楷体', 28), command=Start)
    Star_Button.place(x=360, y=200)
    #######################################################
    LangChoice = tkinter.Frame(root, width=900, height=40)
    LangChoice.pack_propagate(0)  # 固定子窗口的大小
    FromLang_tip = tkinter.Label(LangChoice, text='选择源文本语种', font=('楷体', 18))
    ToLang_tip = tkinter.Label(LangChoice, text='选择译文语种', font=('楷体', 18))
    var_FromLang = tkinter.StringVar(LangChoice)
    var_FromLang.set('英语')
    var_ToLang = tkinter.StringVar(LangChoice)
    var_ToLang.set('中文')
    FromLang = tkinter.OptionMenu(LangChoice, var_FromLang, '自动检测', '中文', '英语', '粤语', '文言文',
                                  '日语', '韩语', '法语', '西班牙语', '泰语',
                                  '阿拉伯语', '俄语', '葡萄牙语', '德语', '意大利语',
                                  '希腊语', '荷兰语', '波兰语', '保加利亚语', '爱沙尼亚语',
                                  '丹麦语', '芬兰语', '捷克语', '罗马尼亚语', '斯洛文尼亚语',
                                  '瑞典语', '匈牙利语', '繁体中文', '越南语')
    FromLang['width'] = 8
    FromLang['height'] = 1
    FromLang.bind(get_FromLang)
    ToLang = tkinter.OptionMenu(LangChoice, var_ToLang, '自动检测', '中文', '英语', '粤语', '文言文',
                                '日语', '韩语', '法语', '西班牙语', '泰语',
                                '阿拉伯语', '俄语', '葡萄牙语', '德语', '意大利语',
                                '希腊语', '荷兰语', '波兰语', '保加利亚语', '爱沙尼亚语',
                                '丹麦语', '芬兰语', '捷克语', '罗马尼亚语', '斯洛文尼亚语',
                                '瑞典语', '匈牙利语', '繁体中文', '越南语')
    ToLang['width'] = 8
    ToLang['height'] = 1
    ToLang.bind(get_ToLang)
    FromLang_tip.place(x=0, y=0)
    FromLang.place(x=175, y=0)
    ToLang_tip.place(x=300, y=0)
    ToLang.place(x=450, y=0)
    #######################################################
    Content_Box = tkinter.Frame(root, width=900, height=160)
    Content_Box.pack_propagate(0)  # 固定子窗口的大小
    var_src_text = tkinter.StringVar()
    var_src_text.set('')
    var_trans_text = tkinter.StringVar()
    var_trans_text.set('')
    input_tips = tkinter.Label(Content_Box, text='在这里输入要翻译的内容', font=('楷体', 18), width=25, height=1)
    result_tips = tkinter.Label(Content_Box, text='翻译结果', font=('楷体', 18), width=25, height=1)
    get_src_text = tkinter.Entry(Content_Box, width=46, textvariable=var_src_text, font=('楷体', 18))
    show_trans_text = tkinter.Entry(Content_Box, width=46, textvariable=var_trans_text, font=('楷体', 18))
    clear_button_src_1 = tkinter.Label(Content_Box, text='x', font=('Consolas', 13), width=4, height=1)
    clear_button_src_1.bind('<Button -1>', clear_src_text)
    clear_button_trans_2 = tkinter.Label(Content_Box, text='x', font=('Consolas', 13), width=4, height=1)
    clear_button_trans_2.bind('<Button -1>', clear_trans_text)
    Trans_Button = tkinter.Button(Content_Box, text='翻译', font=('楷体', 24), width=12, height=2, command=Click_Trans)
    input_tips.place(x=0, y=0)
    get_src_text.place(x=307, y=0)
    result_tips.place(x=0, y=32)
    show_trans_text.place(x=307, y=32)
    clear_button_src_1.place(x=864, y=0)
    clear_button_trans_2.place(x=864, y=32)
    Trans_Button.place(x=312, y=66)
    #########################################################
    History_Box = tkinter.Frame(root, width=900, height=302)
    History_Box.pack_propagate(0)
    HB_tip = tkinter.Label(History_Box, text='展示最近五条翻译记录：', font=('楷体', 18), width=40, height=1)
    # HB_Non_history = tkinter.Label(History_Box, text='没有翻译记录', font=('楷体', 16), width=5, height=1)
    HB_tip.place(x=0, y=0)
    r1 = tkinter.StringVar()
    r1.set(History['1'])
    HB_record1 = tkinter.Entry(History_Box, textvariable=r1, font=('楷体', 18), width=70)
    r2 = tkinter.StringVar()
    r2.set(History['2'])
    HB_record2 = tkinter.Entry(History_Box, textvariable=r2, font=('楷体', 18), width=70)
    r3 = tkinter.StringVar()
    r3.set(History['3'])
    HB_record3 = tkinter.Entry(History_Box, textvariable=r3, font=('楷体', 18), width=70)
    r4 = tkinter.StringVar()
    r4.set(History['4'])
    HB_record4 = tkinter.Entry(History_Box, textvariable=r4, font=('楷体', 18), width=70)
    r5 = tkinter.StringVar()
    r5.set(History['5'])
    HB_record5 = tkinter.Entry(History_Box, textvariable=r5, font=('楷体', 18), width=70)
    record = [[], [HB_record1, 50, r1], [HB_record2, 85, r2], [HB_record3, 120, r3], [HB_record4, 155, r4],
              [HB_record5, 190, r5]]
    #########################################################
    print(translator(src_text))
    root.mainloop()
