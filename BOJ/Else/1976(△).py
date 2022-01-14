# 여행 가자
import sys

input = sys.stdin.readline
N = int(input())
plan_num = int(input())

result = 0
parent = [i for i in range(N+1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x = find(x)
  y = find(y)
  if x < y:
    parent[y] = x
  else:
    parent[x] = y

for i in range(N):
    connection=list(map(int,sys.stdin.readline().split()))
    for j in range(N):#양방향 연결이기때문에
        if connection[j]:#연결하기
            union(i+1,j+1)

isTrue = True
plan = list(map(int,input().split()))
temp = find(plan[0])
for i in range(plan_num):
  if find(plan[i]) != temp:
    isTrue = False
    break

if isTrue:
  print('YES')
else:
  print('NO')