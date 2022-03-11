# 타겟 넘버
def solution(numbers, target):
    answer = 0

    def dfs(target, k, result):
        nonlocal answer
        if k == len(numbers):
            if target == result:
                answer += 1
            return
        else:
            dfs(target, k+1, result+numbers[k])
            dfs(target, k+1, result-numbers[k])

    dfs(target, 0, 0)
    return answer
