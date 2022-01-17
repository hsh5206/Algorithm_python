# 전화번호 목록

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  N = int(input())
  arr = []
  for _ in range(N):
    arr.append(input().strip())
  arr.sort()
  result = 'YES'
  for i in range(N-1):
    leng = len(arr[i])
    if arr[i] == arr[i+1][0:leng]:
      result = 'NO'
      break
  print(result)