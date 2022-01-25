# 시험 감독
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for n in arr:
    n -= B
    result += 1
    if n <= 0:
        continue
    temp = n // C
    result += temp
    n -= temp * C
    if n % C != 0:
        result += 1

print(result)
