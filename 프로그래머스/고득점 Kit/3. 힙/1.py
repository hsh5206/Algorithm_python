# 더 맵게
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) >= 2:
            new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
            heapq.heappush(scoville, new)
            answer += 1
        else:
            answer = -1
            break
    return answer
