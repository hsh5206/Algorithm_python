# 2048 (Easy)

import copy
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = 0


def move_block(arr, n):
    set_result(arr)
    if n == 5:
        # 이동 끝
        return
    for k in range(4):
        temp = copy.deepcopy(arr)
        combine_and_move(temp, k)
        move_block(temp, n+1)


def combine_and_move(arr, k):
    is_combined = [[False] * N for _ in range(N)]
    if k == 0:
        for i in range(N):
            is_combined = [[False] * N for _ in range(N)]
            for j in range(N-1, -1, -1):
                do(i, j, arr, k, is_combined)
    elif k == 1:
        for j in range(N):
            is_combined = [[False] * N for _ in range(N)]
            for i in range(N-1, -1, -1):
                do(i, j, arr, k, is_combined)
    elif k == 2:
        for i in range(N):
            is_combined = [[False] * N for _ in range(N)]
            for j in range(N):
                do(i, j, arr, k, is_combined)
    elif k == 3:
        for j in range(N):
            is_combined = [[False] * N for _ in range(N)]
            for i in range(N):
                do(i, j, arr, k, is_combined)


def do(i, j, arr, k, is_combined):
    dx = dir[k][0]
    dy = dir[k][1]
    if arr[i][j] != 0:
        nx = i + dx
        ny = j + dy
        while 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[nx-dx][ny-dy]
                arr[nx-dx][ny-dy] = 0
            elif arr[nx][ny] == arr[nx-dx][ny-dy] and not is_combined[nx][ny] and not is_combined[nx-dx][ny-dy]:
                is_combined[nx][ny] = True
                arr[nx][ny] *= 2
                arr[nx-dx][ny-dy] = 0
            nx += dx
            ny += dy


def set_result(arr):
    global result
    max_result = 0
    for i in range(N):
        max_result = max(max_result, max(arr[i]))
    result = max(result, max_result)


move_block(arr, 0)
print(result)
