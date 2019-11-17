poker_list = []
for i in range(1,11):
    poker_list.append(['黑桃',str(i)])
    poker_list.append(['红桃', str(i)])
    poker_list.append(['梅花', str(i)])
    poker_list.append(['方块', str(i)])
for i in ('J','Q','K'):
    poker_list.append(['黑桃', i])
    poker_list.append(['红桃', i])
    poker_list.append(['梅花', i])
    poker_list.append(['方块', i])
print(poker_list)