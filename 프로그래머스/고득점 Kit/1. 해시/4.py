# 베스트 앨범
def solution(genres, plays):

    info = [[]for _ in range(len(genres))]
    for i in range(len(plays)):
        info[i] = [genres[i], plays[i], i]
    info.sort(key=lambda x: (-x[1], x[2]))

    hash = dict()
    for genre, number, index in info:
        if hash.get(genre):
            hash[genre][0] += number
            hash[genre][1] += [index]
        else:
            hash[genre] = [number, [index]]

    result = []
    for x in hash.values():
        result.append(x)
    result.sort(reverse=True)

    answer = []
    for _, sings in result:
        answer.append(sings[0])
        if len(sings) >= 2:
            answer.append(sings[1])

    return answer
