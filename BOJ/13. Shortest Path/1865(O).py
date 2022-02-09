# 웜홀
import sys
input = sys.stdin.readline
MAX = sys.maxsize


def bf():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for time, city in arr[i]:
                if times[city] > time + times[i]:
                    times[city] = time + times[i]
                    if k == N:
                        return True
    return False


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    arr = [[]for _ in range(N+1)]
    for _ in range(M):
        a, b, time = map(int, input().split())
        arr[a].append((time, b))
        arr[b].append((time, a))
    for _ in range(W):
        a, b, time = map(int, input().split())
        arr[a].append((-time, b))

    times = [MAX] * (N+1)
    if bf():
        print('YES')
    else:
        print('NO')
