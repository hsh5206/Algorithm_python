# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    visited = set()
    direction = {'R': [0, 1], 'U': [1, 0], 'L': [0, -1], 'D': [-1, 0]}

    # solution
    x, y = 0, 0
    answer = 0
    for order in dirs:
        dx, dy = direction[order]
        if -5 <= x+dx <= 5 and -5 <= y+dy <= 5:
            road1 = ''.join(list(map(str, [x, y, x+dx, y+dy])))
            road2 = ''.join(list(map(str, [x+dx, y+dy, x, y])))
            if road1 not in visited and road2 not in visited:
                answer += 1
            visited.add(road1)
            visited.add(road2)
            x += dx
            y += dy
    return answer


print(solution("LULLLLLLU"))
