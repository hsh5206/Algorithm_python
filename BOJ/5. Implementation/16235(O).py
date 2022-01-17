# 나무 재테크

'''
봄 -> tree의 나이만큼 양분을 먹고 나이 1증가
(같은칸에 여러나무 : 나이가 어린 나무부터 양분을 섭취)
(양분X -> 양분을 먹지못하고 죽음)
여름 -> 죽은 나무가 양분으로 변함 (변한 양분 = 죽은나무나이 // 2)
가을 -> 나무 번식(5의 배수인 나이인 나무만) 인접한 8개의 칸에 나이가 1인 나무 생성
겨울 -> 전체 땅에 양분 추가 (배열만큼씩)

K년 후의 살아있는 나무의 개수를 구하라
'''

import sys
from collections import deque
input = sys.stdin.readline

N, tree_num, K = map(int, input().split())
arr = [[5] * (N) for _ in range(N)]
add = []
for _ in range(N):
    add.append(list(map(int, input().split())))
trees = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(tree_num):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].append(age)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def feed_or_die(i, j):
    tree_len = len(trees[i][j])
    index = 0
    for tree in trees[i][j]:
        if tree > arr[i][j]:
            for _ in range(index, tree_len):
                arr[i][j] += (trees[i][j].pop() // 2)
            break
        else:
            arr[i][j] -= tree
            trees[i][j][index] += 1
            index += 1


def spring_summer():
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]):
                feed_or_die(i, j)


# 번식
def baby_tree(x, y):
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            trees[nx][ny].appendleft(1)


def fall_winter():
    for x in range(N):
        for y in range(N):
            if (len(trees[x][y])):
                for tree in trees[x][y]:
                    if tree % 5 == 0:
                        baby_tree(x, y)
            arr[x][y] += add[x][y]


for _ in range(K):
    spring_summer()
    fall_winter()

result = 0
for i in range(N):
    for j in range(N):
        result += len(trees[i][j])
print(result)
