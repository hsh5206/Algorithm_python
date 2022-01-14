# 사다리 조작

import sys
import copy
input = sys.stdin.readline
N, M, H = map(int, input().split())
arr = [[0] * (N+1) for _ in range(H+1)]

for k in range(1,M+1):
  h, start = map(int,input().split())
  arr[h][start] = k
  arr[h][start+1] = k
result = -1
max = 1


def isTrue(arr):
  for k in range(1,N+1):
    j = k
    s = j
    for i in range(1,H+1):
      if 1<=j<N and arr[i][j] !=0  and arr[i][j+1] == arr[i][j]:
        j += 1
      elif 1<j<=N and arr[i][j] != 0 and arr[i][j-1] == arr[i][j]:
        j -= 1
    if s != j:
      return False
  return True


def makeColumn(x,y,count):
  global result

  if isTrue(arr):
    result = count
    return True

  if count >= max:
    return False

  isFirst = True
  for i in range(x,H+1):
    for j in range(1,N):
      if isFirst:
        j = y
        isFirst = False
      if arr[i][j] == 0 and arr[i][j+1] == 0:
        count += 1
        arr[i][j] = M+count
        arr[i][j+1] = M+count
        if makeColumn(i,j,count):
          return True
        count -= 1
        arr[i][j] = 0
        arr[i][j+1] = 0
  return False

max = 0
isDone = False
for i in range(1,4):
  max += 1
  temp = copy.deepcopy(arr)
  if makeColumn(1,1,0):
    print(result)
    isDone = True
    break

if not isDone:
  print(-1)