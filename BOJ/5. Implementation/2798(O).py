# 블랙잭
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
card = list(map(int, input().split()))

max_result = 0
result = 0
for i in range(N):
    result += card[i]
    for j in range(i+1, N):
        result += card[j]
        for k in range(j+1, N):
            result += card[k]
            if result <= M:
                max_result = max(max_result, result)
            result -= card[k]
        result -= card[j]
    result -= card[i]

print(max_result)
