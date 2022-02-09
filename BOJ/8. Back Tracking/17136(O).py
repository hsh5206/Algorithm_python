# 색종이 붙이기
import sys
import copy
input = sys.stdin.readline
MAX = sys.maxsize

N = 10
arr = []
length_one = 0
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 1:
            length_one += 1
paper = [5] * 6
paper[0] = 0
result = MAX


def check(x, y, nx, ny, arr):
    possible = True
    if 0 <= nx <= N and 0 <= ny <= N:
        for i in range(x, nx):
            for j in range(y, ny):
                if arr[i][j] == 0:
                    possible = False
                    break
            if not possible:
                break
    else:
        possible = False
    return possible


def dfs(a, b, arr, count, delete):
    global result
    if delete == length_one:
        result = min(result, count)
        return
    # 모든 배열을 탐사
    for x in range(a, N):
        for y in range(N):
            # 만약 해당 부분이 1이면
            if arr[x][y] == 1:
                # 사용가능한 종이 고르기
                for p in range(0, len(paper)):
                    if paper[p] == 0:
                        continue
                    # 종이의 범위만큼 지정
                    nx = x + p
                    ny = y + p
                    # 만약 해당 범위가 전부 1이면
                    if check(x, y, nx, ny, arr):
                        # 종이 붙이기
                        d = 0
                        temp = copy.deepcopy(arr)
                        for i in range(x, nx):
                            for j in range(y, ny):
                                temp[i][j] = 0
                                d += 1
                        paper[p] -= 1
                        dfs(x, y, temp, count+1, delete+d)
                        paper[p] += 1
                return


dfs(0, 0, arr, 0, 0)
if result == MAX:
    print(-1)
else:
    print(result)
