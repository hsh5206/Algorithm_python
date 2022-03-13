# 전력난
import heapq
import sys
input = sys.stdin.readline


def prim(road_info, house, start):
    result = 0
    q = []
    heapq.heappush(q, (0, start))
    visited = [False] * house
    while q:
        cost, home = heapq.heappop(q)
        if visited[home]:
            continue
        result += cost
        visited[home] = True
        for ncost, nhome in road_info[home]:
            if not visited[nhome]:
                heapq.heappush(q, (ncost, nhome))
    return result


while True:
    house, road = map(int, input().split())
    if house == 0 and road == 0:
        break

    total_cost = 0
    road_info = [[] for _ in range(house)]
    for _ in range(road):
        x, y, cost = map(int, input().split())
        road_info[x].append((cost, y))
        road_info[y].append((cost, x))
        total_cost += cost

    result = prim(road_info, house, 0)
    print(total_cost - result)
