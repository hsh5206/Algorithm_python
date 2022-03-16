# 주사위 윷놀이
from multiprocessing.dummy import Array


move = list(map(int, input().split()))
horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
road = [[i for i in range(0, 41, 2)], [i for i in range(
    0, 11, 2)]+[13, 16, 19, 25, 30, 35, 40], [i for i in range(0, 25, 2)] + [25, 30, 35, 40], [i for i in range(0, 31, 2)]+[28, 27, 26, 25, 30, 35, 40]]


def back_tracking(x, result, arr):
    global answer
    if x == 10:
        answer = max(answer, result)
        return
    for i in range(x, len(move)):
        for k in range(4):
            # 원래 타입
            road_type_original, _ = horse[k]
            # 바꾼 타입
            change_road(k)
            road_type, now = horse[k]
            # 말이 도착했다면 continue
            if now == -1:
                continue
            # 말이 있다면 continue
            isHorse = False
            for _, temp in horse:
                if now+move[i] == temp:
                    isHorse = True
                    break
            if isHorse:
                continue
            # move
            horse[k][1] += move[i]
            if horse[k][1] >= len(road[road_type]):
                horse[k][1] = -1
                back_tracking(i+1, result, arr + [k, -1])
                horse[k][1] = now
            else:
                back_tracking(
                    i+1, result+road[horse[k][0]][horse[k][1]], arr + [[k, move[i], road[horse[k][0]][horse[k][1]]]])
                horse[k][1] -= move[i]
            horse[k][0] = road_type_original


def change_road(k):
    # 경로 변경
    if horse[k][0] == 0:
        if horse[k][1] == 5:
            horse[k][0] = 1
        elif horse[k][1] == 10:
            horse[k][0] = 2
        elif horse[k][1] == 15:
            horse[k][0] = 3


answer = 0
back_tracking(0, 0, [])
print(answer)
