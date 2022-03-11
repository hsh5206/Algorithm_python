# 여행 경로
def solution(tickets):
    arr = {}
    for start, end in tickets:
        if not arr.get(start):
            arr[start] = [end]
        else:
            arr[start].append(end)
    for temp in arr:
        arr[temp].sort(reverse=True)
    answer = dfs(arr)
    return answer


def dfs(arr):
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in arr or not arr[top]:
            path.append(stack.pop())
        else:
            stack.append(arr[top].pop())
    path.reverse()
    return path
