# 스도쿠
import sys
input = sys.stdin.readline
N = 9
arr = []
zero = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(N):
        if arr[i][j] == 0:
            zero.append((i, j))


def check(x, y, num):
    for j in range(N):
        if arr[x][j] == num:
            return False
    for i in range(N):
        if arr[i][y] == num:
            return False
    temp_x = x // 3 * 3
    temp_y = y // 3 * 3
    for i in range(temp_x, temp_x+3):
        for j in range(temp_y, temp_y+3):
            if arr[i][j] == num:
                return False
    return True


def push_num(count):
    global isDone
    if count == len(zero):
        isDone = True
        return
    x = zero[count][0]
    y = zero[count][1]
    for n in range(1, 10):
        if check(x, y, n):
            arr[x][y] = n
            push_num(count+1)
            if isDone:
                return
            arr[x][y] = 0


isDone = False
push_num(0)
for i in range(N):
    print(*arr[i])
