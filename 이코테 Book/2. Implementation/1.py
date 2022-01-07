# 상하좌우
'''
여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다.
가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.

  L: 왼쪽으로 한 칸 이동
  R: 오른쪽으로 한 칸 이동
  U: 위로 한 칸 이동
  D: 아래로 한 칸 이동

단, N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을 때 여행가 A가 최정적으로 도착할 지점의 좌표를 출력하시오.

입력:
5
R R R U D D

출력:
3 4
'''

N = int(input())
plans = input().split()

dX = [-1, +1, 0, 0]
dY = [0, 0, -1, +1]
move_types = ['L', 'R', 'U', 'D']

x = 1
y = 1
for plan in plans:
    for i in range(len(move_types)):
        if (plan == move_types[i]):
            if(1 <= x+dY[i] and 1 <= y+dX[i] and x+dY[i] <= N and y+dX[i] <= N):
                x += dY[i]
                y += dX[i]
                break
            else:
                continue

print(x, y)
