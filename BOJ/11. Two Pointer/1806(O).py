# 부분합
import sys
MAX = sys.maxsize
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

end = 0
sum = 0
result = MAX
for start in range(N):
    while end < N and sum < S:
        sum += arr[end]
        end += 1
    if sum >= S:
        result = min(result, end-start)
    sum -= arr[start]

if result == MAX:
    print(0)
else:
    print(result)
