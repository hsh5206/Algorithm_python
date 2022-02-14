import heapq


def solution(food_times, K):
    answer = -1
    food = []
    for i in range(len(food_times)):
        heapq.heappush(food, (food_times[i], i+1))

    prev = 0
    l = len(food)
    while food:
        temp = (food[0][0] - prev) * l
        if K >= temp:
            K -= temp
            prev, _ = heapq.heappop(food)
            l -= 1
        else:
            index = K % l
            food.sort(key=lambda x: x[1])
            answer = food[index][1]
            break

    return answer


print(solution([3, 1, 7, 4, 2], 11))
