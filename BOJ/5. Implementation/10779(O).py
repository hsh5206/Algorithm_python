# 쇠막대기

arr = list(input())

result = 0
now = 0
q = []
for i in range(len(arr)):
    if arr[i] == ')':
        if arr[i-1] == '(':
            result += now
        else:
            now -= 1

    else:
        if arr[i+1] != ')':
            now += 1
            result += 1

print(result)
