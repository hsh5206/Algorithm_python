# 순위
def solution(n, results):
    arr = [[0] * (n+1) for _ in range(n+1)]
    for x, y in results:
        arr[x][y] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][j] == 0 and arr[i][k] and arr[k][j]:
                    arr[i][j] = 1
    result = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(1, n+1):
            if i != j:
                sum += arr[i][j] + arr[j][i]
                if sum == n-1:
                    result += 1
    return result
