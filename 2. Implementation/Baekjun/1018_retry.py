# 체스판 다시 칠하기

def paint(arr):
    result = int(1e9)
    min_value = 0
    final = 0
    for i in range(8):
        temp = arr[i][0]
        for j in range(1, 8):
            if temp != arr[i][j] and j % 2 == 0:
                min_value += 1
            elif temp == arr[i][j] and j % 2 == 1:
                min_value += 1
        result = min(min_value, result)
        min_value = 1
        for j in range(1, 8):
            if temp != arr[i][j] and j % 2 == 0:
                min_value += 1
            elif temp == arr[i][j] and j % 2 == 1:
                min_value += 1
        result = min(min_value, result)
        min_value = 0
        final += result
    return final


N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input())

min_value = int(1e9)
for j in range(M - 8):
    temp = []
    for i in range(8):
        temp.append(arr[i][j:j+8])
    result = paint(temp)
    min_value = min(min_value, result)

print(min_value)
