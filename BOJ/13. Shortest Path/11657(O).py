# 타임머신
import sys
input = sys.stdin.readline
MAX = sys.maxsize
N, M = map(int, input().split())
bus = []
for _ in range(M):
    a, b, time = map(int, input().split())
    bus.append((a, b, time))
dist = [MAX] * (N+1)


def bf(start):
    dist[start] = 0
    for k in range(N):
        for i in range(M):
            city, ncity, time = bus[i]
            if dist[city] != MAX and dist[ncity] > dist[city] + time:
                dist[ncity] = dist[city] + time
                if k == N-1:
                    return True
    return False

if bf(1):
  print('-1')
else:
  for i in range(2, N+1):
    if dist[i] == MAX:
      print('-1')
    else:
      print(dist[i])