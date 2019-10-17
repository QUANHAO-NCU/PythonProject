visit = [False for x in range(0, 4)]
ans = [0 for x in range(0, 3)]
count = 0
arr = [1, 2, 3, 4]
#深度优先实现全排列
def dfs(position):
    global count
    if position == len(arr) - 1:
        count += 1
        print(ans)
        return
    for index in range(0,len(arr)):
        if visit[index] == False:
            ans[position] = arr[index]
            visit[index] = True
            dfs(position + 1)
            visit[index] = False
dfs(0)
print('\n', count)