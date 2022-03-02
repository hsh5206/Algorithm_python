# 다리를 지나는 트럭
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck = deque(0 for _ in range(bridge_length))
    truck_weights.reverse()

    now_weight = 0
    while truck_weights:
        answer += 1
        temp = truck.popleft()
        if temp != 0:
            now_weight -= temp
        if now_weight + truck_weights[-1] <= weight:
            t = truck_weights.pop()
            truck.append(t)
            now_weight += t
        else:
            truck.append(0)
    answer += bridge_length
    return answer


print(solution(2, 10, [7, 4, 5, 6]))
