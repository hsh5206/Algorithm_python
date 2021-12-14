# 기둥과 보

def solution(N, build_frame):
    result = [[0] * 3 for _ in range(N+1)]
    for i in range(len(build_frame)):
        x, y, struc, do = build_frame[i]
        if do == 0:  # 삭제
            if struc == 0:

    return result


arr = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1, ],
       [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
solution(5, arr)
