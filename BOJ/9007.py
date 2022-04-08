# 카누 선수
T = int(input())
for _ in range(T):
    k, n = map(int, input().split())
    arr = []
    for _ in range(4):
        arr.append(list(map(int, input().split())))

    left, right = 1, int(1e7)*4
    while left <= right:
        mid = (left+right)//2
