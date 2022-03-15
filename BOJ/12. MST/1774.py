# 우주신과의 교감
import math
import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())


def prim(start):
    result = 0
    visited = [False] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if visited[node]:
            continue
        visited[node] = True
        result += dist
        for ndist, nnode in arr[node]:
            heapq.heappush(q, (ndist, nnode))
    return result


# 노드 위치 정보
nodes = [[]]
for _ in range(N):
    nodes.append(list(map(int, input().split())))

# 이미 연결되어 있는 값을 저장
connected = set()
for _ in range(M):
    x, y = map(int, input().split())
    connected.add((x, y))
    connected.add((y, x))

# 연결리스트
arr = [[] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(i+1, N+1):
        # 이미 연결되어 있다면 dist를 0으로
        if (i, j) in connected:
            arr[i].append((0, j))
            arr[j].append((0, i))
            continue
        # 연결 되지 않았다면
        dist = math.sqrt((nodes[i][0]-nodes[j][0])**2 +
                         (nodes[i][1]-nodes[j][1])**2)
        arr[i].append((dist, j))
        arr[j].append((dist, i))

print("%.2f" % prim(1))
