# 동전 0
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

result = 0
for x in arr:
    if K == 0:
        break
    if x <= K:
        result += K // x
        K = K % x

print(result)
