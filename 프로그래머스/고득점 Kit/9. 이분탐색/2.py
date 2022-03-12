# 징검다리
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 1, distance
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        other_rock = 0
        for rock in rocks:
            if rock - other_rock < mid:
                temp += 1
            else:
                other_rock = rock
        if temp > n:
            end = mid - 1
        elif temp <= n:
            answer = mid
            start = mid + 1
    return answer
