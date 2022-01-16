# 분해합

N = int(input())
min_result = int(1e9)
result = 0
for i in range(1, N):
    result += i
    temp = 0
    arr = str(i)
    for j in range(len(arr)):
        temp += int(arr[j])
    result += temp
    if result == N:
        min_result = min(min_result, i)
    result -= temp
    result -= i

if min_result == int(1e9):
    print(0)
else:
    print(min_result)
