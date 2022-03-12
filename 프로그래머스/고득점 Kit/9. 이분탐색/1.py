# 입국심사
def solution(n, times):
    answer = 0
    times.sort()
    left, right = 1, max(times)*n
    while left <= right:
        mid = (left+right)//2
        temp = 0
        for time in times:
            temp += mid // time
        if temp >= n:
            answer = mid
            right = mid - 1
        elif temp < n:
            left = mid + 1
    return answer
