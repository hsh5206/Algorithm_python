# 음료수 얼려 먹기

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    global arr
    node = arr[x][y]
    if node == 0:
        arr[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, 0)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False


N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)
