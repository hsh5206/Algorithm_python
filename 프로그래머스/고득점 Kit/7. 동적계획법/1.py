# N으로 표현
def solution(N, number):
    arr = [0]
    for i in range(1, 9):
        temp = make(i, N, arr)
        if number in temp:
            return i
        arr.append(temp)
    return -1


def make(i, N, arr):
    result = set()
    temp = int(str(N) * i)
    result.add(temp)
    for half in range(1, i//2+1):
        for x in arr[half]:
            for y in arr[i-half]:
                result.add(x+y)
                result.add(x-y)
                result.add(y-x)
                result.add(x*y)
                if y != 0:
                    result.add(x//y)
                if x != 0:
                    result.add(y//x)
    return result
