# 퍼즐
from collections import deque
N = 3
arr = []
zero_x = 0
zero_y = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 0:
            zero_x = i
            zero_y = j
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visit = dict()


def bfs(a, b):
    global arr
    q = deque()
    string = change(arr)
    if string == '123456780':
        return '0'
    q.append((a, b, 0, string))
    visit[string] = True
    while q:
        x, y, count, string = q.popleft()
        if string == '123456780':
            return count
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                index = x*3+y
                next_index = nx*3+ny
                next_string = list(string)
                next_string[index] = next_string[next_index]
                next_string[next_index] = '0'
                next_string = ''.join(next_string)
                if not visit.get(next_string):
                    visit[next_string] = True
                    q.append((nx, ny, count+1, next_string))
    return False


def change(arr):
    string = ''
    for i in range(N):
        for j in range(N):
            string += str(arr[i][j])
    return string


result = bfs(zero_x, zero_y)
if result:
    print(result)
else:
    print(-1)
