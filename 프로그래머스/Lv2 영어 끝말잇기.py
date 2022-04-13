# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    access_list = set()
    before = words[0][0]
    cnt, fin_idx = 0, 0
    isFin = False
    for idx, word in enumerate(words):
        if idx % n == 0:
            cnt += 1
        if before[-1] == word[0] and word not in access_list:
            access_list.add(word)
            before = word
        else:
            isFin = True
            fin_idx = idx
            break
    if isFin:
        return [fin_idx % n+1, cnt]
    else:
        return [0, 0]
