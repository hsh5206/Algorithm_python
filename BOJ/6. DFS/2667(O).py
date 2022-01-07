# 단지번호붙이기
N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))


def dfs(x, y, result):
    nx = x
    ny = y
    if nx <= -1 or nx >= N or ny <= -1 or ny >= N:
        return result
    elif arr[nx][ny] == 0:
        return result
    else:
        result += 1
        x = nx
        y = ny
        arr[x][y] = 0
        result = dfs(x - 1, y, result)
        result = dfs(x + 1, y, result)
        result = dfs(x, y - 1, result)
        result = dfs(x, y + 1, result)
    return result


result = 0
count_list = []
for i in range(N):
    for j in range(N):
        result = 0
        add = dfs(i, j, result)
        if add != 0:
            count_list.append(add)

count_list.sort()
print(len(count_list))

for count in count_list:
    print(count)
