# 이중 우선순위 큐
import heapq

T = int(input())
for _ in range(T):
    N = int(input())
    min_heap = []
    max_heap = []
    visited = [False] * N
    for idx in range(N):
        order, data = input().split()
        data = int(data)
        if order == 'I':
            heapq.heappush(min_heap, (data, idx))
            heapq.heappush(max_heap, (-data, idx))
            visited[idx] = True
        elif order == 'D':
            if data == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    data, idx = heapq.heappop(max_heap)
                    visited[idx] = False
            elif data == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    data, idx = heapq.heappop(min_heap)
                    visited[idx] = False

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
