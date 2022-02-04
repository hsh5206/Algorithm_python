# 음악프로그램
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
front = [0] * (N+1)
arr = [[] for _ in range(N+1)]
for i in range(1, M+1):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]):
        arr[temp[j]].append(temp[j+1])
        front[temp[j+1]] += 1

result = []
for _ in range(N):
    for i in range(1, N+1):
        if front[i] == 0 and i not in result:
            result.append(i)
            for j in range(len(arr[i])):
                front[arr[i][j]] -= 1

if len(result) == N:
    print(*result, sep='\n')
else:
    print('0')
