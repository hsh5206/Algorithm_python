# 오등큰수
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)
result = [-1] * N
stack = []

for i in range(N):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
