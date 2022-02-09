# 괄호 추가하기
import sys
input = sys.stdin.readline
N = int(input())
arr = input().strip()
nums = []
op = []


def calculate(arr):
    return eval(arr)


def dfs(arr):
    global result
    result = max(result, calculate(arr))


result = 0
dfs(arr)
print(result)
