# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'creat the word book'
__author__ = 'QuanHao'
import sqlite3


def creatWordBook(self):
    wordbook = [(1, 'python', '蟒蛇'),
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
                (17, 'figure', '体型'), ]
    conn = sqlite3.connect('WordBook.db')  # 连接到数据库
    cursor = conn.cursor()  # 创建游标
    conn.execute(
        'create table WordBook (id varchar (20) primary key,word varchar(20)),chineseMean varchar (100)')  # 创建单词表,id为主键
    conn.executemany('insert into WordBook (id,word,chineseMean) values(?,?,?)', wordbook)  # 输入单词数据
    cursor.close()
    conn.commit()
    conn.close()
    # select 语句返回所有匹配的记录，每一条记录是一个元组


if __name__ != '__main__':
    creatWordBook()
