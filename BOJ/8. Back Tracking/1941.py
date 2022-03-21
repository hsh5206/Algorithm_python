# 소문난 칠공주

from collections import defaultdict
import sys
input = sys.stdin.readline
arr = []
for _ in range(5):
    arr.append(list(input().strip()))
visited = defaultdict(bool)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def back_tracking(people):
    global result
    # (해당 people의 숫자를 arr좌표상의 문자열로 바꿔서 문자열로 join)의 'Y'의 개수
    if (''.join([arr[i//5][i % 5] for i in people]).count('Y')) > 3:
        return
    # 7명이라면
    if len(people) == 7:
        # people을 정렬
        temp = sorted(people)
        # 문자열로 바꾸고
        temp_str = ''.join(list(map(str, temp)))
        # 딕셔너리에 없으면 result += 1
        if temp_str not in visited:
            visited[temp_str] = True
            result += 1
        return
    for person in people:
        # 0번부터 24번인 person을 좌표로 바꿔줌
        x = person // 5
        y = person % 5
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5:
                # 좌표를 다시 0번부터 24번으로 바꿔줌
                person_num = nx*5+ny
                if person_num not in people:
                    people.append(person_num)
                    back_tracking(people)
                    people.pop()


result = 0
for i in range(25):
    back_tracking([i])
print(result)
