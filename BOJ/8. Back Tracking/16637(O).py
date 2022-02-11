# 괄호 추가하기
import copy
import sys
input = sys.stdin.readline
MAX = sys.maxsize

N = int(input())
arr = input().strip()
nums = []
op = []
for i, x in enumerate(arr):
    if i % 2 == 0:
        nums.append(x)
    else:
        op.append(x)


def calculate(a, op, b):
    return str(eval(a+op+b))


def calculate_front(arr):
    result = arr[0]
    for i in range(1, len(arr)-1, 2):
        result = calculate(result, arr[i], arr[i+1])
    return result


def dfs(index, arr, is_used):
    global answer
    if index == len(op):
        answer = max(answer, int(calculate_front(arr)))
        return
    if is_used:
        temp = copy.deepcopy(arr)
        temp.append(op[index])
        temp.append(nums[index+1])
        dfs(index+1, temp, False)
    else:
        temp = copy.deepcopy(arr)
        temp.append(op[index])
        temp.append(nums[index+1])
        dfs(index+1, temp, False)
        temp.pop()
        temp.pop()
        temp.pop()
        temp.append(calculate(nums[index], op[index], nums[index+1]))
        dfs(index+1, temp, True)


answer = -MAX
dfs(0, [nums[0]], False)
print(answer)
