# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for target in s:
        if target == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(target)
    return True if not stack else False


print(solution("()()"))
