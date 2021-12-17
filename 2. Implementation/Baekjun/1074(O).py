# Z
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)
N, r, c = map(int, input().split())


def search(n, x, y, result):
    if n == 1:
        result += (2*x + y)
        return result
    if n // 2 <= x:
        if n // 2 <= y:
            temp = n//2
            result += ((temp)**2)*3
            result = search(temp, x - temp, y - temp, result)
        else:
            temp = n//2
            result += ((temp)**2)*2
            result = search(temp, x - temp, y, result)
    else:
        if n // 2 <= y:
            temp = n//2
            result += ((temp)**2)*1
            result = search(temp, x, y - temp, result)
        else:
            temp = n//2
            result += ((temp)**2)*0
            result = search(temp, x, y, result)
    return result


result = search(2**N, r, c, 0)

print(result)
