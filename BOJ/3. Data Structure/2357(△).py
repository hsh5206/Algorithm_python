# 최솟값과 최댓값
import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int, input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
tree = [[MAX, 0] for _ in range(N+1)]
tree2 = [[MAX, 0] for _ in range(N+1)]


def update(i, target):
    while i <= N:
        tree[i][0] = min(tree[i][0], target)
        tree[i][1] = max(tree[i][1], target)
        i += (i & -i)


def update2(i, target):
    while i > 0:
        tree2[i][0] = min(tree2[i][0], target)
        tree2[i][1] = max(tree2[i][1], target)
        i -= (i & -i)


def find(start, end):
    result_min = MAX
    result_max = 0
    prev = start
    curr = prev + (prev & -prev)
    while curr <= end:
        result_min = min(result_min, tree2[prev][0])
        result_max = max(result_max, tree2[prev][1])
        prev = curr
        curr = prev + (prev & -prev)
    result_min = min(result_min, arr[prev])
    result_max = max(result_max, arr[prev])

    prev = end
    curr = prev - (prev & -prev)
    while curr >= start:
        result_min = min(result_min, tree[prev][0])
        result_max = max(result_max, tree[prev][1])
        prev = curr
        curr = prev - (prev & -prev)

    print(result_min, result_max)


for i, x in enumerate(arr):
    if i > 0:
        update(i, x)
        update2(i, x)

for _ in range(M):
    start, end = map(int, input().split())
    find(start, end)
