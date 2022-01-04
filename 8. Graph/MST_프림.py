# 프림 알고리즘

import sys
import heapq
input = sys.stdin.readline

# 노드수, 간선수
V, E = map(int, input().split())
# 인접리스트
edge = [[] for _ in range(V+1)]
# 방문확인
chk = [False] * (V+1)
# 양방향 그래프
for i in range(E):
    a, b, cost = map(int, input().split())
    edge[a].append((cost, b))
    edge[b].append((cost, a))

# 1번노드에서 출발 현재비용: 0
heap = [[0, 1]]
rs = 0
while heap:
    cost, node = heap.heappop(heap)
    # 방문을 안했다면
    if chk[node] == False:
        chk[node] = True  # 방문체크
        rs += cost  # 비용 추가
        # 연결된 모든 간선들 중
        for next_edge in edge[node]:
            # 방문 안했다면 힙에 추가
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)
