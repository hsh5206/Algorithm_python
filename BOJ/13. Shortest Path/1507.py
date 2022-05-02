# 궁금한 민호

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

road = [[True]*N for _ in range(N)]

# 플로이드 와샬 역으로
result = 0
for k in range(N):
    for i in range(N):
        if i != k:
            for j in range(N):
                if i != j and k != j:
                    if arr[i][j] == arr[i][k]+arr[k][j]:
                        road[i][j] = False
                    elif arr[i][j] > arr[i][k]+arr[k][j]:
                        result = -1

if not result:
    for i in range(N):
        for j in range(i, N):
            if road[i][j]:
                result += arr[i][j]

print(result)
