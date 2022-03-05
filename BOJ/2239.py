# 스도쿠
import sys
input = sys.stdin.readline
N = 9
arr = []
empty = []
for i in range(N):
    arr.append(list(input().strip()))
    for j in range(N):
        if arr[i][j] == '0':
            empty.append((i, j))


def add_num(k):
    global isDone
    if k == len(empty):
        isDone = True
        return
    temp = check_available_num(empty[k][0], empty[k][1])
    for x in temp:
        arr[empty[k][0]][empty[k][1]] = x
        add_num(k+1)
        if isDone:
            return
        arr[empty[k][0]][empty[k][1]] = '0'


def check_available_num(x, y):
    temp = []
    for target in range(1, N+1):
        target = str(target)
        if check_rcs(x, y, target):
            temp.append(target)
    return temp


def check_rcs(x, y, target):
    for j in range(N):
        if arr[x][j] == target:
            return False
    for i in range(N):
        if arr[i][y] == target:
            return False
    temp_x = x // 3 * 3
    temp_y = y // 3 * 3
    for i in range(temp_x, temp_x+3):
        for j in range(temp_y, temp_y+3):
            if arr[i][j] == target:
                return False
    return True


isDone = False
add_num(0)
for i in range(N):
    print(''.join(arr[i]))
