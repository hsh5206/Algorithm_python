def solution(absolutes, signs):
    answer = ['+'+str(j) if i else '-'+str(j)
              for i, j in zip(signs, absolutes)]
    answer = ''.join(answer)
    return eval(answer)
