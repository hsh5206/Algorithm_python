# 감시

import sys
import copy
input = sys.stdin.readline
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 0->동 / 1->서 / 2->남 / 3->북
dir = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]],
       [[0, 2], [2, 1], [1, 3], [3, 0]], [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
result = sys.maxsize


def fill(x, y, arr, dir):
    for d in dir:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break


def dfs(arr, cnt):
    global result
    temp = copy.deepcopy(arr)
    if cnt == cctv_cnt:
        num = 0
        for i in range(N):
            num += temp[i].count(0)
        result = min(result, num)
        return
    x, y, cctv = q[cnt]
    for i in dir[cctv]:
        fill(x, y, temp, i)
        dfs(temp, cnt+1)
        temp = copy.deepcopy(arr)


cctv_cnt = 0
q = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            q.append([i, j, arr[i][j]])
            cctv_cnt += 1


dfs(arr, 0)
print(result)
