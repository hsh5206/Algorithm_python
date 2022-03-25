# 친구비
import sys
import heapq
input = sys.stdin.readline
N, M, k = map(int, input().split())
arr = [[]for _ in range(N+1)]
moneys = [0]+list(map(int, input().split()))
for i in range(1, N+1):
    arr[0].append((moneys[i], i))
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append((0, b))
    arr[b].append((0, a))


def make_friend():
    global answer
    q = []
    heapq.heappush(q, (0, 0))
    visited = [False] * (N+1)
    while q:
        money, node = heapq.heappop(q)
        if not visited[node]:
            visited[node] = True
            answer += money
            if answer > k:
                return False
            for nmoney, nnode in arr[node]:
                if not visited[nnode]:
                    heapq.heappush(q, (nmoney, nnode))
    return True


answer = 0
if make_friend():
    print(answer)
else:
    print('Oh no')
