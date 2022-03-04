# K번째수
def solution(array, commands):
    answer = []
    for start, end, k in commands:
        sliced = array[start-1:end]
        sliced.sort()
        answer.append(sliced[k-1])
    return answer
