# 이중 우선순위 큐
import heapq


def solution(operations):
    max_heap = []
    min_heap = []
    visited = [False] * len(operations)
    for i, oper in enumerate(operations):
        order, num = oper.split()
        num = int(num)
        # push
        if order == 'I':
            heapq.heappush(min_heap, [num, i])
            heapq.heappush(max_heap, [-num, i])
        # pop
        if order == 'D':
            if num == 1:
                if max_heap:
                    is_ok(max_heap, visited)
            else:
                if min_heap:
                    is_ok(min_heap, visited)

    answer = [0, 0]
    if min_heap:
        number, index = heapq.heappop(min_heap)
        while min_heap and visited[index]:
            number, index = heapq.heappop(min_heap)
        if not visited[index]:
            answer[0] = number
            answer[1] = number
    if max_heap:
        number, index = heapq.heappop(max_heap)
        while max_heap and visited[index]:
            number, index = heapq.heappop(max_heap)
        if not visited[index]:
            answer[0] = -number
            if answer[1] == 0:
                answer[1] = -number

    return answer


def is_ok(heap, visited):
    number, index = heapq.heappop(heap)
    while heap and visited[index]:
        number, index = heapq.heappop(heap)
    visited[index] = True
