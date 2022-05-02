# 회전 초밥
from collections import defaultdict
N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr += arr[:k-1]

left, right = 0, k
result = 0
dict = defaultdict(int)
dict[c] += 1

for x in arr[left:right]:
    dict[x] += 1

while right < len(arr):
    result = max(result, len(dict))
    dict[arr[left]] -= 1
    dict[arr[right]] += 1
    if dict[arr[left]] == 0:
        dict.pop(arr[left])
    left += 1
    right += 1

print(result)
