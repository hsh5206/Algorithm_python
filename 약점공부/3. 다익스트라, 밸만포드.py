# 다익스트라 알고리즘
# 한 노드에서 다른 노드로 가는 모든 최단 경로(1차원 리스트)
# Greedy 계열
# O(ElogV)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한값

# 노드의 수, 간선의 수
n, m = map(int, input().split())
# 시작노드
start = int(input())
# 각 노드의 연결되어 있는 노드에 대한 정보 2차원리스트
graph = [[] for _ in range(n+1)]
# 최단거리 테이블
distance = [INF]*(n+1)
# 간선의 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작노드에서 시작노드로 가는 최단 경로는 0, 큐에 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))  # (최단경로, 인덱스)
    while q:
        # 가장 최단 거리 노드 pop
        dist, now = heapq.heappop(q)
        # 노드가 이미 처리 됐으면
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]  # cost = 나의 비용 + i[0]으로 이동하는 비용인 i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:  # 해당 노드의 비용 (i[0] -> 노드)
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print[distance[i]]


# 벨만포드 알고리즘
def bf(time, times, arr, N):
    # 모든 노드 탐색 (N-1번 반복)
    # 만약 N번째에도 최단거리 갱신이 된다면 음의 순환 존재
    for k in range(1, N+1):
        # 모든 노드의 연결된 간선 확인
        for i in range(1, N+1):
            for time, city in arr[i]:
                # 해당 간선이 최단 거리이면 초기화
                if times[city] > time + times[i]:
                    times[city] = time + times[i]
                    # 만약 N번째 라운드라면 음수 순환 존재 return True
                    if k == N:
                        return True
    return False
