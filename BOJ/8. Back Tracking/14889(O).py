# 스타트와 링크

import sys
MAX = sys.maxsize
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

people = [i for i in range(N)]
start_team = []
result = MAX


def chooseMember(num, k):
    global result
    if num == N//2:
        link_team = []
        link_team = list(set(people) - set(start_team))
        result = min(result, abs(getScore(link_team) - getScore(start_team)))
        return
    for i in range(k, N):
        start_team.append(i)
        chooseMember(num+1, i+1)
        start_team.pop()


def getScore(list):
    score = 0
    for node in range(N):
        if node in list:
            for nnode in range(len(arr[node])):
                if nnode in list and node != nnode:
                    score += arr[node][nnode]
    return score


chooseMember(0, 0)
print(result)
