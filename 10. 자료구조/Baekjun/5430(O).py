# AC

import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    error = False

    do = input().strip()
    N = int(input())
    array = input()
    arr = array[1:(len(array)-2)].split(',')

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()

    reverse = False
    for k in range(len(do)):
        if do[k] == 'R':
            reverse = not reverse
        else:
            if not arr:
                print("error")
                error = True
                break
            if reverse:
                arr.pop()
            else:
                arr.popleft()

    if reverse:
        arr.reverse()
    if not error:
        print("[", end="")
        for i in range(len(arr)):
            print(arr[i], end="")
            if i == len(arr)-1:
                break
            print(",", end="")
        print("]")
