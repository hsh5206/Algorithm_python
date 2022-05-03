from itertools import product as pro


def solution(word):
    result = []
    for i in range(1, 6):
        for x in pro(['A', 'E', 'I', 'O', 'U'], repeat=i):
            result.append(''.join(list(x)))
    result.sort()
    return result.index(word)+1
