# 호텔

C, N = map(int, input().split())
arr = []
for _ in range(N):
    cost, customer = map(int, input().split())
    efficiency = cost / customer
    arr.append((efficiency, cost, customer))

arr.sort()

result = int(1e9)
for x in arr:
