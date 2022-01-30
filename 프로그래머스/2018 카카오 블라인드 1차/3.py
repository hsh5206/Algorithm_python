# 캐시
from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            for i in range(len(cache)):
                if cache[i] == city:
                    cache.remove(city)
                    break
            cache.append(city)
        else:
            answer += 5
            if cacheSize != 0:
                if cache and len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
    return answer
