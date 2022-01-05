# 맥주 마시면서 걸어가기
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        if abs(x - A) + abs(y - B) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = conv[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    q.append([nx, ny])
                    visited[i] = True
    print("sad")


t = int(input())
for _ in range(t):
    n = int(input())
    q = deque()

    conv = []
    a, b = map(int, input().split())
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    A, B = map(int, input().split())
    visited = [False for _ in range(n+1)]

    bfs()
