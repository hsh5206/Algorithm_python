# 텀 프로젝트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def dfs(s, n):
    global result
    if visited[s]:
        return
    visited[s] = True
    haveTeam.append(s)
    if student[s]-1 in haveTeam:
        temp = haveTeam[haveTeam.index(student[s]-1):]
        result += temp
        return
    dfs(student[s]-1, n+1)


T = int(input())
for _ in range(T):
    N = int(input())
    student = list(map(int, input().split()))
    result = []
    visited = [False] * N

    for i in range(N):
        if not visited[i]:
            haveTeam = [i]
            visited[i] = True
            while True:
                if visited[student[i]-1]:
                    break
                haveTeam.append(student[i]-1)
                visited[i] = True
                if student[i]-1 in haveTeam:

    print(N-len(result))
