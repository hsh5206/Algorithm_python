# 구간 합 구하기
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

tree = [0]*(N*4+1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start, mid, index*2)+init(mid+1, end, index*2+1)
    return tree[index]


def change(start, end, index, where, diff):
    if where < start or where > end:
        return
    tree[index] += diff
    if start != end:
        mid = (start+end)//2
        change(start, mid, index*2, where, diff)
        change(mid+1, end, index*2+1, where, diff)


def rangeSum(start, end, left, right, index):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[index]
    mid = (start+end)//2
    return rangeSum(start, mid, left, right, index*2)+rangeSum(mid+1, end, left, right, index*2+1)


init(1, N, 1)
for _ in range(M+K):
    type, a, b = map(int, input().split())
    if type == 1:
        diff = b-arr[a]
        arr[a] = b
        change(1, N, 1, a, diff)
    else:
        result = rangeSum(1, N, 1, a, b)
        print(result)
