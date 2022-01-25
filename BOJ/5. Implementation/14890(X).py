# 경사로
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
result = 0


def check():
    global result
    for i in range(N):
        isOK = True
        isSlope = [False] * N
        for j in range(1, N):
            if abs(arr[i][j-1]-arr[i][j]) > 1:
                isOK = False
                break
            elif abs(arr[i][j-1]-arr[i][j]) == 0:
                continue
            else:
                if slope_check(i, j, isSlope):
                    continue
                else:
                    isOK = False
                    break
        if isOK:
            result += 1


def row_slope_check(i, j, isSlope):
    n = 0
    if arr[i][j] > arr[i][j+1]:
        temp = arr[i][j]
        while 0 <= j < N and n < L and not isSlope[j]:
            if arr[i][j+1] == temp:
                isSlope[j] = True
            else:
                break
            j += 1
    else:
        temp = arr[i][j+1]
        while 0 < j < N and n <= L and not isSlope[j]:
            if arr[i][j-1] == arr[i][j]:
                temp += 1
                isSlope[j] = True
            else:
                break
            j -= 1
    if temp == L:
        return True
    return False


def column_slope_check(i, j, isSlope):
    temp = 1
    if arr[i-1][j] > arr[i][j]:
        while 0 <= i < N-1 and temp <= L and not isSlope[i]:
            if arr[i+1][j] == arr[i][j]:
                isSlope[i] = True
                temp += 1
            else:
                break
            i += 1
    else:
        i -= 1
        while 0 < i < N and temp <= L:
            if arr[i-1][j] == arr[i][j] and not isSlope[i]:
                isSlope[i] = True
                temp += 1
            else:
                break
            i -= 1
    if temp == L:
        return True
    return False


def check_column():
    global result
    for j in range(N):
        isOK = True
        isSlope = [False] * N
        for i in range(1, N):
            if abs(arr[i-1][j]-arr[i][j]) > 1:
                isOK = False
                break
            elif abs(arr[i-1][j]-arr[i][j]) == 0:
                continue
            else:
                if column_slope_check(i, j, isSlope):
                    continue
                else:
                    isOK = False
                    break
        if isOK:
            result += 1


check_row()
check_column()
print(result)
