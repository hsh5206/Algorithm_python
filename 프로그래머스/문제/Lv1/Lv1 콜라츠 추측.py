# https://programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    cnt = 0
    while num != 1:
        num = num//2 if not num % 2 else num*3+1
        cnt += 1
    return cnt if cnt < 500 else -1
