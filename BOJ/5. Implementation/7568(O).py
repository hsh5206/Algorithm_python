# 덩치
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    kg, cm = map(int, input().split())
    arr.append((kg, cm))
result = [0] * N

for i in range(N):
    cnt = 1
    for j in range(N):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt += 1
    result[i] = cnt

for i in range(N):
    print(result[i], end=' ')
