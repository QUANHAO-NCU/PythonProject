import jieba
import jieba.analyse
import numpy

with open('三国演义.txt', 'r+', encoding='utf-8') as f:
    content = f.read()
    words = jieba.lcut(content, cut_all=False)
    counts = {}
    # keywords = jieba.analyse.extract_tags(content, topK=20, withWeight=True, allowPOS=('nr'))
    # for item in keywords:
    #     print(item[0], item[1])
    # 基于TF-IDF进行的关键词 词频分析
    for word in words:
        rword = word
        if len(word) == 1:
            continue
        elif word == '诸葛亮' or word == '孔明曰':
            rword = '孔明'
        elif word == '关公' or word == '云长':
            rword == '关羽'
        elif word == '玄德' or word == '玄德曰':
            rword = '刘备'
        elif word == '孟德' or word == '丞相':
            rword = '曹操'
        word=rword
        counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    personlist = ['孔明','曹操','张飞','刘备','关羽','孙权','吕布','鲁肃','赵云','马超','姜维','魏延'\
                  ,'庞统','董卓','袁绍','黄忠','孟获','陆逊','孙尚香','孙坚','孙策','司马懿','曹丕','张辽','典韦']
    with open('result.txt', 'w+', encoding='utf-8') as result:
        for i in range(100):
            word, count = items[i]
            if word in personlist:
                print('{0:<10}{1:>5}'.format(word, count))
                result.write(word + '     ' + str(count)+'\n')
