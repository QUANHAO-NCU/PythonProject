# 实验01 猜单词初始python
import random

word_list = ['answer', 'python', 'hello', 'world', 'environment', 'event', 'external']
end_process = ''
print('{: ^40}\n{: ^40}'.format('欢迎参加猜单词游戏', '请把下列各字母组合成一个正确的单词。'))


def end(end_flag):
    if (end_flag == 'N' or end_flag == 'n'):
        return 0
    elif (end_flag == 'Y' or end_flag == 'y'):
        return 1
    else:
        print('输入字符错误！')


while (True):
    get_or_word = word_list[random.randint(0, len(word_list) - 1)]
    random_word = get_or_word
    # 从单词表选取源单词
    out_of_order_word = ''
    for i in range(len(get_or_word)):
        position = random.randint(0, len(random_word) - 1)
        out_of_order_word += random_word[position]
        random_word = random_word[:position] + random_word[(position + 1):]
    print('乱序的单词是：' + out_of_order_word)
    if (input('请你猜：') != get_or_word):
        print('对不起不正确！')
        while (input('继续猜：') != get_or_word):
            print('对不起不正确！')
    print('真棒！你猜对了！')
    if (end(input('是否继续？Y/N:'))):
        continue
    else:
        break
