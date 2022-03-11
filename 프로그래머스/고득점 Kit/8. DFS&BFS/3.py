# 단어 변환
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    return answer


def bfs(begin, target, words):
    visited = [False] * len(words)
    q = deque()
    q.append((begin, 0))
    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            if visited[i] == True:
                continue
            diff = 0
            for x, y in zip(word, words[i]):
                if x != y:
                    diff += 1
            if diff == 1:
                q.append((words[i], cnt + 1))
    return 0
