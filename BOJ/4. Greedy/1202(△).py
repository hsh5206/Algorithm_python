# 보석 도둑
import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
gem = []
for _ in range(N):
    weight, cost = map(int, input().split())
    heapq.heappush(gem, (weight, cost))

bags = []
for _ in range(K):
    w = int(input())
    bags.append(w)
bags.sort()

result = 0
temp = []
for bag_weight in bags:
    while gem:
        if bag_weight >= gem[0][0]:
            weight, cost = heapq.heappop(gem)
            heapq.heappush(temp, -cost)
        else:
            break
    if temp:
        result -= heapq.heappop(temp)
print(result)
