from collections import deque
import sys


def solution(n, wires):
    answer = sys.maxsize
    for i in range(len(wires)):
        new_wires = wires[:i] + wires[i+1:]
        arr = [[]for _ in range(n+1)]
        for x, y in new_wires:
            arr[x].append(y)
            arr[y].append(x)
        visited = [False for _ in range(n+1)]
        result = []
        for k in range(1, n+1):
            if not visited[k]:
                result.append(counting(n, arr, visited, k))
        answer = min(answer, abs(result[0] - result[1]))
    return answer if answer != sys.maxsize else -1


def counting(n, arr, visited, k):
    q = deque()
    q.append(k)
    visited[k] = True
    cnt = 1
    while q:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt
