# https://programmers.co.kr/learn/courses/30/lessons/12950
def solution(arr1, arr2):
    answer = [[x+y for x, y in zip(_arr1, _arr2)]
              for _arr1, _arr2 in zip(arr1, arr2)]
    return answer
