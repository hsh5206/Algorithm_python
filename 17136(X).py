# 색종이 붙이기
import sys
input = sys.stdin.readline
N = 10
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
paper = [5] * 5
paper[0] = 0


def check(x, y, nx, ny):
    isZero = False
    if 0 <= nx < N and 0 <= ny < N:
        for i in range(x, nx):
            for j in range(y, ny):
                if arr[i][j] == 0:
                    isZero = True
                    break
            if isZero:
                break
    return not isZero


def dfs(x, y):
    global result
    did = False
    for p in range(len(paper)):
        if paper[p] == 0:
            continue
        nx = x + p
        ny = y + p
        if check(x, y, nx, ny):
            # 종이 붙이기
            did = True
            for i in range(x, nx):
                for j in range(y, ny):
                    arr[i][j] = 0
            paper[p] -= 1
            result += 1
            break
    return did


result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if not dfs(i, j):
                print(-1)
                exit(0)
print(result)
