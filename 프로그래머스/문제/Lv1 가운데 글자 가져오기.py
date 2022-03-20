def solution(s):
    s, leng = list(s), len(s)
    answer = ''
    if leng % 2 == 0:
        answer = ''.join(s[leng//2-1:leng//2+1])
    else:
        answer = ''.join(s[leng//2:leng//2+1])
    return answer
