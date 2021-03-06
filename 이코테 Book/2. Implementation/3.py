# 왕실의 나이트
'''
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다.
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.
나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

  1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
  2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

8x8 평면상에서 나이트의 위치가 주여졌을 때, 나이트가 이동할 수 있는 경우의 수를 출력하시오.
단, 행의 위치는 1~8, 열의 위치는 a~h로 표현한다.

입력:
a1

출력:
2
'''

temp = input()
row = int(temp[1])
column = int(ord(temp[0])) - int(ord('a')) + 1
count = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if(next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8):
        count += 1

print(count)
