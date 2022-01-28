# K번째 수

N = int(input())
K = int(input())

start, end = 1, K
result = 0
while start <= end:
    mid = (start+end) // 2
    index = 0
    for i in range(1, N+1):
        index += min(mid//i, N)
    if index >= K:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
print(result)
