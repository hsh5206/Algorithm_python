# 경로 찾기

import sys
input = sys.stdin.readline
N = int(input())
arr = [] * N
for _ in range(N):
    arr.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                if arr[i][k] + arr[k][j] == 2:
                    arr[i][j] = 1

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()
