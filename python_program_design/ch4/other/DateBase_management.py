import sqlite3

conn = sqlite3.connect('../mindGame-qh6110116148.db')  # 链接数据库
cursor = conn.cursor()  # 打开游标
# 创建数据库
conn.execute(
    'create table if not exists QA (id varchar(20) primary key, question varchar(40),Answer_A varchar(40),Answer_B varchar(40),Answer_C varchar(40), Answer_D varchar(40), right_Answer varchar(10))')
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('哈雷慧星的平均周期为', '54年', '56年', '73年', '83年', 'C')")
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('夜郎自大中“夜郎”指的是现在哪个地方？', '贵州', '云南', '广西', '福建', 'A')")
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('在中国历史上是谁发明了麻药', '孙思邈', '华佗', '张仲景', '扁鹊', 'B')")
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('京剧中花旦是指', '年轻男子', '年轻女子', '年长男子', '年长女子', 'B')")
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('篮球比赛每队几人？', '4', '5', '6', '7', 'B')")
cursor.execute("insert into QA (question, Answer_A,Answer_B,Answer_C,Answer_D,right_Answer) values ('在天愿作比翼鸟，在地愿为连理枝。讲述的是谁的爱情故事？', '焦钟卿和刘兰芝', '梁山伯与祝英台', '崔莺莺和张生', '杨贵妃和唐明皇', 'D')")

conn.commit()
cursor.close()
conn.close()
