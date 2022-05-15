# 순회강연
import sys
input = sys.stdin.readline

N = int(input())
info = []

max_day = 0
for _ in range(N):
    pay, day = map(int, input().split())
    max_day = max(max_day, day)
    info.append((day, pay))
info.sort(key=lambda i: (i[1], i[0]))

possible = [True for i in range(max_day+1)]
result = 0
for _ in range(N):
    day, pay = info.pop()
    for d in range(day, 0, -1):
        if possible[d]:
            possible[d] = False
            result += pay
            break

print(result)
