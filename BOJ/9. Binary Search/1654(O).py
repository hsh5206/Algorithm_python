# 랜선 자르기
import sys

K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)

while start <= end:
    line = 0
    mid = (start + end) // 2
    for x in arr:
        line += x // mid
    if line < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
