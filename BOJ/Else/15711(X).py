# 환상의 짝꿍

from math import sqrt
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    total = x + y
    arr = [i for i in range(2000001)]

    for i in range(2, int(sqrt(total))+1):
        j = 2
        while True:
            if i * j >= total:
                break
            arr[i*j] = 0
            j += 1
    result = "NO"
    for i in range(1, total):
        if arr[i] != 0 and arr[total-i] != 0:
            result = "YES"
            break

    print(result)
