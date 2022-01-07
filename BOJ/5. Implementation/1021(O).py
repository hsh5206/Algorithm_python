# 회전하는 큐

from collections import deque
N, M = map(int, input().split())

q = deque()
arr = list(map(int, input().split()))
for i in range(N):
    q.append(0)
    for j in range(M):
        if i+1 == arr[j]:
            q[i] = j+1

count = 0
for i in range(1, M+1):
    for j in range(N):
        if i == q[j]:
            if j <= len(q) // 2:
                for _ in range(j):
                    q.append(q.popleft())
                    count += 1
                q.popleft()
                break
            else:
                for _ in range(len(q) - j):
                    q.appendleft(q.pop())
                    count += 1
                q.popleft()
                break

print(count)
