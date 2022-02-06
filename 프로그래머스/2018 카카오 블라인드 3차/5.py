def solution(words):
    answer = 0
    for i in range(len(words)):
        word = words[i]
        isBreak = False
        count = 0
        while True:
            for j in range(len(words)):
                if i == j:
                    continue
                if word in words[j]:
                    if count != 0:
                        answer += 1
                    answer += len(word)
                    isBreak = True
                    break
            if not isBreak:
                word = word[:-1]
                count += 1
            else:
                break
    return answer


print(solution(["go", "gone", "guild"]))
