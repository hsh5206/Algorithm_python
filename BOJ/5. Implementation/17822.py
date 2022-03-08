# 원판 돌리기
from collections import deque
import sys
intput = sys.stdin.readline
N, M, T = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

arr = []
for _ in range(N):
    arr.append(deque(map(int, input().split())))

order = []
for _ in range(T):
    order.append(list(map(int, input().split())))


def rolling(n, dir):
    for x in range(n, N+1, n):
        if dir == 0:
            temp = arr[x-1].pop()
            arr[x-1].appendleft(temp)
        else:
            temp = arr[x-1].popleft()
            arr[x-1].append(temp)


def breaking():
    change = []
    for i in range(N):
        for j in range(M):
            now = arr[i][j]
            if now == 'x':
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if ny == -1 or ny == M:
                    if ny == -1:
                        ny = M-1
                    else:
                        ny = 0
                if 0 <= nx < N and 0 <= ny < M:
                    if now == arr[nx][ny]:
                        change.append((i, j))
                        change.append((nx, ny))
    if change:
        changing(change)
        return True
    else:
        return False


def changing(change):
    for x, y in change:
        arr[x][y] = 'x'


def dividing():
    sum = 0
    leng = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'x':
                sum += arr[i][j]
                leng += 1
    if leng == 0:
        return
    avg = sum / leng
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 'x':
                if arr[i][j] > avg:
                    arr[i][j] -= 1
                elif arr[i][j] < avg:
                    arr[i][j] += 1


for x, dir, k in order:
    for _ in range(k):
        rolling(x, dir)
    if not breaking():
        dividing()

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] != 'x':
            result += arr[i][j]
print(result)
