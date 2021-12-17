# 카드 정렬하기

import heapq
N = int(input())
q = []
for _ in range(N):
    heapq.heappush(q, int(input()))

result = 0
if N == 1:
    heapq.heappop(q)
while q:
    if len(q) == 1:
        x = heapq.heappop(q)
        result += x
        break
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    temp = a + b
    result += temp
    if len(q) != 0:
        heapq.heappush(q, temp)

print(result)
