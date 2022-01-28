# 후위 표기식
from collections import deque
from re import L
notAlpha = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}

alpha = deque()
sign = []


def popAll():
    while alpha:
        result.append(alpha.popleft())
    x = sign.pop()
    while sign:
        temp = sign.pop()
        if x == ')' and temp == '(':
            break
        if temp == '(':
            sign.append(temp)
            break
        if notAlpha[x] <= notAlpha[temp]:
            result.append(temp)
        else:
            sign.append(temp)
            break
    if x != ')':
        sign.append(x)


arr = list(input().strip())
result = []
temp = []
isParen = 0
for x in arr:
    if x not in notAlpha:
        alpha.append(x)
    else:
        sign.append(x)
        if sign[-1] == ')':
            popAll()
        if len(sign) > 1 and sign[-1] != '(' and notAlpha[sign[-1]] <= notAlpha[sign[-2]]:
            popAll()

while alpha:
    result.append(alpha.popleft())
while sign:
    result.append(sign.pop())
print(*result, sep='')
