# 로봇 청소기

N, M = map(int, input().split())
r, c, direction = map(int, input().split())

clean = [[0]*M for _ in range(N)]

loc = [0 for _ in range(N)]
for i in range(N):
    loc[i] = list(map(int, input().split()))

moveR = [-1, 0, 1, 0]
moveC = [0, 1, 0, -1]


def change_dir():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
clean[r][c] = 1

flag = 0
while(True):
    change_dir()
    nr = r+moveR[direction]
    nc = c+moveC[direction]
    if(loc[nr][nc] == 0 and clean[nr][nc] == 0):
        r = nr
        c = nc
        clean[r][c] = 1
        count += 1
        flag = 0
        continue
    else:
        flag += 1
    if flag == 4:
        # 뒤로
        nr = r-moveR[direction]
        nc = c-moveC[direction]
        if loc[nr][nc] == 0:
            r = nr
            c = nc
        else:
            break
        flag = 0

print(count)
