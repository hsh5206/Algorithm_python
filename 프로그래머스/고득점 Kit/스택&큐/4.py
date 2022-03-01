# 주식가격
def solution(prices):

    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, pri in enumerate(prices):
        while stack and prices[stack[-1]] > pri:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    while stack:
        index = stack.pop()
        answer[index] = len(prices) - 1 - index

    return answer
