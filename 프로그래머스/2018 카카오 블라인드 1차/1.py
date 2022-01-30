# 비밀지도
def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = bin(i | j)[2:]
        while len(temp) < n:
            temp = '0' + temp
        temp = temp.replace('0', ' ')
        temp = temp.replace('1', '#')
        answer.append(temp)
    return answer
