from collections import deque


def solution(n, wires):
    answer = int(1e9)
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]
        arr = [[]for _ in range(n+1)]
        for x, y in temp:
            arr[x].append(y)
            arr[y].append(x)
        visited = [False for _ in range(n+1)]
        result = []
        for k in range(1, n+1):
            if not visited[k]:
                result.append(counting(n, arr, visited, k))
        if len(result) == 2:
            answer = min(answer, abs(result[0] - result[1]))
    return answer if answer != int(1e9) else -1


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


print(solution(9, [[1, 3], [2, 3], [3, 4], [
      4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
