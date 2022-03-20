# 마법사 상어와 파이어볼
import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball_info = []
for _ in range(M):
    x, y, big, speed, dir = map(int, input().split())
    fireball_info.append([x, y, big, speed, dir])


def fireball_move():
    # fireball의 좌표를 집합으로 관리 (중복값없게)
    fireballs = set()
    # 각 위치별 fireball 표시
    temp = [[[] for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(len(fireball_info)):
        x, y, big, speed, dir = fireball_info.pop()
        nx = x + dx[dir] * speed
        ny = y + dy[dir] * speed
        # 적절한 fireball 위치 반환
        nx, ny = move_place(nx, ny)
        # 이동한 좌표를 fireballs 집합에 추가
        fireballs.add((nx, ny))
        # temp의 해당 위치에 fireball 정보 추가
        temp[nx][ny].append((big, speed, dir))
    # 위치별 fireball개수 파악
    fireball_spread(fireballs, temp)


def move_place(x, y):
    if 1 <= x <= N and 1 <= y <= N:
        return x, y
    if x > N:
        x = x % N
    if x < 1:
        x = N-abs(x) % N
    if y > N:
        y = y % N
    if y < 1:
        y = N-abs(y) % N
    return x, y


def fireball_spread(fireballs, temp):
    # 모든 fireball의 위치마다 실시
    for x, y in fireballs:
        # 파이어볼이 한개이면 fireball_info에 추가
        if len(temp[x][y]) == 1:
            big, speed, dir = temp[x][y].pop()
            fireball_info.append([x, y, big, speed, dir])
            continue
        # 파이어볼이 2개 이상이면
        leng = len(temp[x][y])
        sum_big, sum_speed, dirs = 0, 0, []
        while temp[x][y]:
            big, speed, dir = temp[x][y].pop()
            sum_big += big
            sum_speed += speed
            dirs.append(dir)
        # 새로운 질량
        new_big = sum_big // 5
        # 만약 질량이 0이면 파이어볼 소멸
        if new_big == 0:
            continue
        # 새로운 스피드
        new_speed = sum_speed // leng
        # 새로운 방향 결정
        even, odd = 0, 0
        isOK = True
        for d in dirs:
            if d % 2 == 0:
                even += 1
            else:
                odd += 1
            if even and odd:
                isOK = False
                break
        # 모두 짝수이거나 홀수이면
        if isOK:
            for nd in [0, 2, 4, 6]:
                fireball_info.append((x, y, new_big, new_speed, nd))
        # 아니라면
        else:
            for nd in [1, 3, 5, 7]:
                fireball_info.append((x, y, new_big, new_speed, nd))


for _ in range(K):
    fireball_move()

result = 0
for _, _, big, _, _ in fireball_info:
    result += big
print(result)
