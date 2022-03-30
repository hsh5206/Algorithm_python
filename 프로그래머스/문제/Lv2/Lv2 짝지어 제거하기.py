# https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    answer = 0 if can_remove(list(s)) else 1
    return answer


def can_remove(s):
    stack = []
    for x in s:
        if not stack:
            stack.append(x)
        else:
            if stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
    return stack
