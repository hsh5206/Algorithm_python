# 오큰수
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N
stack = []

for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
