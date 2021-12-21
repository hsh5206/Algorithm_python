# 부분수열의 합
from itertools import combinations
N, K = map(int, input().split())

arr = list(map(int, input().split()))

count = 0
result = 0
for i in range(1, N+1):
    for x in combinations(arr, i):
        result = 0
        for k in range(len(x)):
            result += x[k]
        if result == K:
            count += 1

print(count)
