# 최솟값
import sys
input = sys.stdin.readline
MAX = sys.maxsize

N, M = map(int, input().split())
arr = [0]
for _ in range(N):
    arr.append(int(input()))


def update(i, target):
    while i <= N:
        tree[i] = min(tree[i], target)
        i += (i & -i)


def update2(i, target):
    while 0 < i:
        tree2[i] = min(tree2[i], target)
        i -= (i & -i)


def find(start, end):
    result = MAX

    prev = start
    curr = prev + (prev & -prev)
    while curr <= end:
        result = min(result, tree2[prev])
        prev = curr
        curr = prev + (prev & -prev)
    result = min(result, arr[prev])

    prev = end
    curr = prev - (prev & -prev)
    while curr >= start:
        result = min(result, tree[prev])
        prev = curr
        curr = prev - (prev & -prev)

    return result


tree = [MAX] * (N+1)
tree2 = [MAX] * (N+1)
for i, x in enumerate(arr):
    if i > 0:
        update(i, x)
        update2(i, x)

for _ in range(M):
    start, end = map(int, input().split())
    print(find(start, end))
