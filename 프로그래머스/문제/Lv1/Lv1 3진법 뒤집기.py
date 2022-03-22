def solution(n):
    temp = ''
    while n:
        temp += str(n % 3)
        n = n//3
    return int(temp, 3)
