# 감시 피하기
'''
5
X S S S X
T X X S X
X T X S X
X X T X S
X X X T X
'''

from collections import deque
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input().split()))

T_num = 0
teacher = deque()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            T_num += 1
            teacher.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def search():
    result = True
    for _ in range(T_num):
        a, b = teacher.popleft()
        teacher.append((a, b))
        q = deque()
        for i in range(4):
            x, y = a, b
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'X':
                    q.append((nx, ny, dx[i], dy[i]))
                elif arr[nx][ny] == 'S':
                    result = False
                    return result
        while q:
            x, y, wx, wy = q.popleft()
            nx = x + wx
            ny = y + wy
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'X':
                    q.append((nx, ny, dx[i], dy[i]))
                elif arr[nx][ny] == 'S':
                    result = False
                    return result
    return result


def dfs(count):
    global fin
    if count == 3:
        fin = search()
        if fin == True:
            return
        return
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                count += 1
                dfs(count)
                if fin == True:
                    return
                arr[i][j] = 'X'
                count -= 1


dfs(0)
if fin == True:
    print('YES')
else:
    print('NO')
