# 친구
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(input()))


def friend(arr, result, me, who):
    for i in range(N):
        if i == who or i == me:
            continue
        if arr[who][i] == 'Y':
            if i not in result:
                result.append(i)


final = -1
result = []
for i in range(N):
    result = []
    for j in range(N):
        if i == j:
            continue
        if arr[i][j] == 'Y':
            result.append(j)
    temp = len(result)
    for x in range(temp):
        friend(arr, result, i, result[x])
    final = max(final, len(result))

print(final)
