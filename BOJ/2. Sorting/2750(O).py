# 수 정렬하기
N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

arr.sort()
for k in arr:
  print(k)