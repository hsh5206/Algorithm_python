# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        index = []
        for x in skill:
            i = tree.find(x)
            if i != -1:
                index.append((i, x))
        index.sort()
        result = ''
        for _, x in index:
            result += x
        if result and result[0] == skill[0] and result in skill:
            answer += 1
        elif not result:
            answer += 1
    return answer
