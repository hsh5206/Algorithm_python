# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    sum_x = sum(list(map(int, str(x))))
    return True if not x % sum_x else False
