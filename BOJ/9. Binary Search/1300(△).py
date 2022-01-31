# K번째 수
N = int(input())
k = int(input())

start, end = 1, k
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in range(1, N+1):
        count += min(N, mid // i)
    if count >= k:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
