# 거짓말
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
know = set(map(int, input().split()[1:]))
party = []
for _ in range(M):
    people = set(map(int, input().split()[1:]))
    party.append(people)

can = [True] * M
for _ in range(M):
    for i, people in enumerate(party):
        if people & know:
            can[i] = False
            know = know | people

result = 0
for i in range(M):
    if can[i]:
        result += 1
print(result)
