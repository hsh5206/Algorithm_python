# https://programmers.co.kr/learn/courses/30/lessons/77485

import sys


def solution(rows, columns, queries):
    arr = [[(i)*columns+(j+1) for j in range(columns)] for i in range(rows)]
    result = []
    for x1, y1, x2, y2 in queries:
        result.append(change(x1-1, y1-1, x2-1, y2-1, arr))
    return result


def change(x1, y1, x2, y2, arr):
    min_value = sys.maxsize
    # 맨 위 맨 왼쪽 기록
    temp = arr[x1][y1]
    # 왼쪽
    for k in range(x1, x2):
        arr[k][y1] = arr[k+1][y1]
        min_value = min(min_value, arr[k+1][y1])
    # 아래
    for k in range(y1, y2):
        arr[x2][k] = arr[x2][k+1]
        min_value = min(min_value, arr[x2][k+1])
    # 오른쪽
    for k in range(x2, x1, -1):
        arr[k][y2] = arr[k-1][y2]
        min_value = min(min_value, arr[k-1][y2])
    # 위
    for k in range(y2, y1+1, -1):
        arr[x1][k] = arr[x1][k-1]
        min_value = min(min_value, arr[x1][k-1])
    # 기록했던 값 업데이트
    arr[x1][y1+1] = temp
    min_value = min(min_value, temp)
    return min_value
