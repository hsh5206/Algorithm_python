# 플로이드 와샬 알고리즘
# 모든 노드에서 모든 노드로 가는 최단경로 (2차원 리스트)
# DP 계열
# O(N^3)

INF = int(1e9)

# 노드 수, 간선 수
n = int(input())
m = int(input())

# 2차원 리스트(그래프)
graph = [[INF] * (n+1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달 할 수 없는 경우, 무한출력
        if graph[a][b] >= INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b])
    print()
