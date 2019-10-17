# 实验01 猜单词初始python
import random
import sqlite3

# word_list = ['answer', 'python', 'hello', 'world', 'environment', 'event', 'external']
#########################################################################################
wordlist = [(1, 'python', '蟒蛇'),
            (2, 'absorb', '吸收'),
            (3, 'edition', '版本'),
            (4, 'complain', '抱怨'),
            (5, 'economic', '经济的'),
            (6, 'psychological', '心理的'),
            (7, 'concrete', '混凝土'),
            (8, 'evidence', '证据'),
            (9, 'overseas', '海外的'),
            (10, 'elaborate', '精巧的'),
            (11, 'failure', '失败者'),
            (12, 'release', '释放'),
            (13, 'minimum', '最少的'),
            (14, 'current', '当前的'),
            (15, 'strain', '负担'),
            (16, 'civil', '公民的'),
            (17, 'figure', '体型')]
conn = sqlite3.connect('WordBook.db')  # 连接到数据库
cursor = conn.cursor()  # 创建游标
try:
    conn.execute(
    'create table WordBook (id varchar (20) primary key,word varchar(20),chineseMean varchar (100))')  # 创建单词表,id为主键
    conn.executemany('insert into WordBook (id,word,chineseMean) values(?,?,?)', wordlist)  # 输入单词数据,数据写在一个列表中
except:
    pass#数据库已存在则继续程序
conn.commit()
cursor.close()
conn.close()  # 关闭游标指针
# 数据库的创建
#########################################################################################
WordBook = sqlite3.connect('WordBook.db')  # 连接到数据库
WB_cursor = WordBook.cursor();  # 创建游标
maxLines = list(WB_cursor.execute('select count(*) from WordBook'))[0][0]  # 获取数据库的行数，确定随机选取单词的范围
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
    get_or_word = list(WB_cursor.execute('select id,word,chineseMean from WordBook where id = ?',\
                                         (str(random.randint(1,maxLines+1)),)))[0][1]
    random_word = get_or_word
    # 从单词表数据库中选取源单词
    out_of_order_word = ''
    for i in range(len(get_or_word)):
        position = random.randint(0, len(random_word) - 1)
        out_of_order_word += random_word[position]
        random_word = random_word[:position] + random_word[(position + 1):]
    #     将源单词生成乱序单词
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
