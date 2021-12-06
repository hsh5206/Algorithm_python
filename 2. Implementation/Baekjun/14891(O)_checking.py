# 톱니바퀴
'''
8개 톱니
S / N
옆의 톱니바퀴의 극이 다르면
반대로 회전
같으면
회전X
옆이 회전 안하면
회전X

1 -> 1번 톱니바퀴
2 -> 2번 톱니바퀴
3 -> 3번 톱니바퀴
4 -> 4번 톱니바퀴
12시방향부터 시계방향으로 주어진다
N극은 0 S극은 1
5 -> 회전횟수 K
K -> 회전 방법 순서대로 (회전시킬 톱니바퀴 번호, 방향) 방향 -> 시계 1 반시계 -1
.
.
.

12시방향 N극 이면 0 S극이면 각 1,2,4,8 점
의 점수 합
'''

# 앞에서부터 12시 -> 1.5시 -> 3시 -> 4.5시 -> 6시 -> 7.5시 -> 9시 -> 10.5시 //8개 의 N(1)/S(0)
topni = [0*8 for _ in range(4)]
for i in range(4):
    topni[i] = list(input())

for i in range(4):
    for j in range(8):
        topni[i][j] = int(topni[i][j])

K = int(input())  # 회전횟수
how = []
# how[i] = [n번톱니바퀴, 시계(1)/반시계(-1)]
for i in range(K):
    how.append(list(map(int, input().split())))

# 회전함수


def turn(mainT, dir, start):  # flag 회전유무
    if(mainT >= 0 and mainT <= 3):
        # 첫실행일때
        if start == mainT:
            if mainT == 0:
                if topni[mainT][2] != topni[mainT+1][6]:
                    turn(mainT+1, -dir, start)

            elif mainT == 1:
                if topni[mainT][2] != topni[mainT+1][6]:
                    turn(mainT+1, -dir, start)
                if topni[mainT][6] != topni[mainT-1][2]:
                    turn(mainT-1, -dir, start)

            elif mainT == 2:
                if topni[mainT][2] != topni[mainT+1][6]:
                    turn(mainT+1, -dir, start)
                if topni[mainT][6] != topni[mainT-1][2]:
                    turn(mainT-1, -dir, start)

            elif mainT == 3:
                if topni[mainT][6] != topni[mainT-1][2]:
                    turn(mainT-1, -dir, start)

        # 오른쪽으로만 진행
        elif(start < mainT):
            if mainT == 1:
                if topni[mainT][2] != topni[mainT+1][6]:
                    turn(mainT+1, -dir, start)

            elif mainT == 2:
                if topni[mainT][2] != topni[mainT+1][6]:
                    turn(mainT+1, -dir, start)

           # 왼쪽으로만 진행
        elif(start > mainT):
            if mainT == 1:
                if topni[mainT][6] != topni[mainT-1][2]:
                    turn(mainT-1, -dir, start)

            elif mainT == 2:
                if topni[mainT][6] != topni[mainT-1][2]:
                    turn(mainT-1, -dir, start)

        # 시계방향
        if(dir == 1):
            temp1 = topni[mainT][0]
            for i in range(8):
                if i+1 == 8:
                    topni[mainT][0] = temp1
                else:
                    temp = topni[mainT][i+1]
                    topni[mainT][i+1] = temp1
                    temp1 = temp
        # 반시계방향
        elif(dir == -1):
            temp1 = topni[mainT][0]
            for i in range(8):
                temp = topni[mainT][7-i]
                topni[mainT][7-i] = temp1
                temp1 = temp


for i in range(K):
    # how확인
    mainT = how[i][0] - 1  # n번 톱니바퀴
    dir = how[i][1]  # 회전방향
    turn(mainT, dir, mainT)


result = 0
for i in range(4):
    if(topni[i][0] == 1):
        if i == 0:
            result += 1
        elif i == 1:
            result += 2
        elif i == 2:
            result += 4
        elif i == 3:
            result += 8

print(result)
