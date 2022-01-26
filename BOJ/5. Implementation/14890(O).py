# 경사로
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
result = 0


def check(line):
    global result
    isOK = True
    isSlope = [False] * N
    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i] - line[i+1]) >= 2:
            isOK = False
            break
        elif abs(line[i] - line[i+1]) == 1:
            if slope_check(line, i, isSlope):
                continue
            else:
                isOK = False
                break
    if isOK:
        result += 1


def slope_check(line, i, isSlope):
    n = 0

    if line[i] > line[i+1]:
        temp = line[i+1]
        i = i+1
        while 0 <= i < N and n < L and not isSlope[i]:
            if line[i] == temp:
                isSlope[i] = True
                n += 1
            else:
                break
            i += 1

    elif line[i] < line[i+1]:
        temp = line[i]
        while 0 <= i < N and n < L and not isSlope[i]:
            if line[i] == temp:
                isSlope[i] = True
                n += 1
            else:
                break
            i -= 1

    if n == L:
        return True
    return False


# row 체크
for i in range(N):
    check(arr[i])
# column 체크
for j in range(N):
    temp = []
    for i in range(N):
        temp.append(arr[i][j])
    check(temp)

print(result)
