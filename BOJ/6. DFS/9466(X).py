# 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(s, n):
    visited[s] = True
    haveTeam.append(s)
    if student[s]-1 in haveTeam:
        temp = haveTeam[haveTeam.index(student[s]-1):]
        print(temp)
        return temp

    dfs(student[s]-1, n+1)


T = int(input())
for _ in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    haveTeam = []
    result = []
    visited = [False] * N
    for i in range(N):
        if not visited[i]:
            result.append(dfs(i, 0))

    answer = N - len(result)
    print(answer)
