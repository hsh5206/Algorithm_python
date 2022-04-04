# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    for k in range(len(s)):
        temp = s[k:]+s[:k]
        if check(temp):
            answer += 1
    return answer


def check(temp):
    arr = list(temp)
    if arr[0] in (')', '}', ']'):
        return False
    if arr[-1] in ('(', '{', '['):
        return False

    dict = {')': '(', '}': '{', ']': '['}
    stack = []
    for x in arr:
        if not stack:
            stack.append(x)
        elif x in dict.keys() and stack[-1] == dict[x]:
            stack.pop()
        else:
            stack.append(x)
    if stack:
        return False
    return True
