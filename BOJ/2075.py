# N번째 큰 수
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    temp = list(map(int, input().split()))

    if i == 0:
        for x in temp:
            heapq.heappush(heap, x)
        continue

    for x in temp:
        if heap[0] < x:
            heapq.heappop(heap)
            heapq.heappush(heap, x)

print(heap[0])
