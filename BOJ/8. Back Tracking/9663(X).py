# N-Queen

N = int(input())
arr = [[0] * N for _ in range(N)]
result = 0
count = 0
dx = [0, -1, 0, 1, 1, -1, -1, 1]
dy = [1, 0 - 1, 0, 1, -1, 1, -1]


def dfs(arr, count, a, b):
    global result

    if count == N:
        result += 1
        for i in arr:
            print(i)
        print()
        return

    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = arr[i][j]

    i = a
    j = b
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = 2
                count += 1
                paint(i, j)
                dfs(arr, count, i, j)
                for a in range(N):
                    for b in range(N):
                        arr[a][b] = temp[a][b]
                count -= 1


def paint(x, y):
    for i in range(N):
        arr[x][i] = 1
        arr[i][y] = 1
        if x+i < N and y+i < N:
            arr[x+i][y+i] = 1
        if 0 <= x-i and 0 <= y-i:
            arr[x-i][y-i] = 1
        if x+i < N and 0 <= y-i:
            arr[x+i][y-i] = 1
        if 0 <= x-i and y+i < N:
            arr[x-i][y+i] = 1
    arr[x][y] = 2


dfs(arr, count, 0, 0)
print(result)
