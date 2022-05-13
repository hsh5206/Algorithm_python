# 택배
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
box_num = int(input())
box_info = []
for _ in range(box_num):
    start, end, num = map(int, input().split())
    box_info.append((start, end, num))
box_info.sort(key=lambda x: (x[1]))

result = 0
arr = [W for _ in range(N+1)]
for x, y, num in box_info:
    num = min(num, min(arr[x:y]))
    if num != 0:
        for i in range(x, y):
            arr[i] -= num
        result += num

print(result)
