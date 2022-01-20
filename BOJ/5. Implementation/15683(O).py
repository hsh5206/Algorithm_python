# 감시
'''
0 빈칸

cctv
1번 = 한쪽방향 (동 / 남 / 서 / 북)
2번 = 두방향 (동서 / 남북)
3번 = 두방향 (동남 / 남서 / 서북 / 북동)
4번 = 세방향 (동남서 / 남서북 / 서북동 / 북동남)
5번 = 네방향 (동서남북)
[동:0, 남:1, 서:2, 북:3]

6 벽

# 감지가능
'''

import sys
import copy
input = sys.stdin.readline
N, M = map(int, input().split())

MAX = sys.maxsize
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

cctv = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [
    [0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * M for _ in range(N)]
result = MAX
cctv_count = 0

cctvs = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctvs.append((i, j, arr[i][j]))


def see(cctv_count, arr):
    global result

    if cctv_count == len(cctvs):
        result = min(result, count(arr))
        return

    x, y, what = cctvs[cctv_count]
    for dir in cctv[what]:
        temp = copy.deepcopy(arr)
        for k in dir:
            nx = x + dx[k]
            ny = y + dy[k]
            while 0 <= nx < N and 0 <= ny < M:
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'
                elif temp[nx][ny] == 6:
                    break
                nx += dx[k]
                ny += dy[k]
        see(cctv_count+1, temp)


def count(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count


temp = copy.deepcopy(arr)
see(0, temp)
print(result)
