# 디스크 컨트롤러
import heapq


def solution(jobs):
    leng = len(jobs)
    jobs.sort(reverse=True)
    heap = []
    now, answer = 0, 0
    while heap or jobs:
        if heap:
            temp = heapq.heappop(heap)
            answer += now + temp[0] - temp[1]
            now += temp[0]
        for i in range(len(jobs)-1, -1, -1):
            start, dur = jobs[i]
            if now >= start:
                s, dur = jobs.pop()
                heapq.heappush(heap, [dur, s])
            else:
                if not heap:
                    now += 1
                break
    answer //= leng
    return answer
