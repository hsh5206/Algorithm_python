# 연료 채우기

'''
  1km -> 1L
  N개 주유소 (연료 get) // 거리, 연료양
  마을까지 운전

  L 마을 까지 거리
  P 처음 연료 양

  heapq (거리, 연료양)
if 현재 연료양 < 거리:
  불가능
  if q
    전에놈을 팝해서 사용
    result += 1
    q.popall
else:
  q.append(거리, 연료양)


'''
import sys
import heapq
heap = []
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    heapq.heappush(heap, list(map(int, input().split())))
final, now = map(int, input().split())
heapq.heappush(heap, [final, 0])
where = 0

q = []
result = 0
while heap:
    dist, value = heapq.heappop(heap)
    if now < abs(where - dist):
        if q:
            heapq.heappush(heap, [dist, value])
            value, dist = heapq.heappop(q)
            value = -value
            now += value
            result += 1
        else:
            break
    else:
        now -= abs(where - dist)
        where += abs(where - dist)
        heapq.heappush(q, (-value, dist))

if where == final and now >= 0:
    print(result)
else:
    print(-1)
