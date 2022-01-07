# 예산
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end = max(arr)

result = 0
while start <= end:
    budget = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            budget += mid
        else:
            budget += x
    if budget > M:
        end = mid - 1
    else:
        start = mid + 1
        result = budget

print(end)
