# 유기농 배추

T = int(input())


def dfs(x, y):
    nx = x
    ny = y
    if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
        return False
    if arr[nx][ny] == 0:
        return False
    else:
        x = nx
        y = ny
        arr[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True


for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                count += 1

    print(count)
