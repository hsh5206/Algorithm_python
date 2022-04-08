# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for x in numbers:
        x = int(x)  # 7,8,9번 런타임 에러 문제의 입력 오류
        arr = list('0'+bin(x)[2:])
        index = ''.join(arr).rfind('0')
        arr[index] = '1'
        if x % 2 != 0:
            arr[index+1] = '0'
        answer.append(int(''.join(arr), 2))
    return answer
