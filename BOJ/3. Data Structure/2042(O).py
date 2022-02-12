# 구간 합 구하기
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append(int(input()))
tree = [0] * (N+1)


def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & -i)


def fromOne_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)
    return result


def print_sum(start, end):
    print(fromOne_sum(end) - fromOne_sum(start-1))


for i, x in enumerate(arr):
    if i > 0:
        update(i, x)

for _ in range(M+K):
    type, a, b = map(int, input().split())
    if type == 1:
        diff = b - arr[a]
        update(a, diff)
        arr[a] = b
    else:
        print_sum(a, b)
