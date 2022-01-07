# 주사위 굴리기

# 지도-NxM 주사위위치-x,y 명령어개수-K
N, M, x, y, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

moveX = [0, 0, 0, -1, 1]
moveY = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]

top = 1
for i in order:
    nx = x + moveX[i]
    ny = y + moveY[i]
    # 값 이동
    # 범위 내라면
    if nx < N and 0 <= nx and ny < M and 0 <= ny:
        # 이동
        x = nx
        y = ny

        if i == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif i == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif i == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        # 이동한 위치값이 0이면
        if(maps[x][y] == 0):
            # 주사위바닥_값 복사
            maps[x][y] = dice[5]
            # 탑의 값 초기화
        elif(maps[x][y] != 0):
            # 칸의 수가 바닥으로 복사 칸은 0이된다
            dice[5] = maps[x][y]
            maps[x][y] = 0

        # 탑 출력
        print(dice[0])
    else:
        continue
