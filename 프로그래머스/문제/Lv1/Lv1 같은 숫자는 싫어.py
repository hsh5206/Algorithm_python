def solution(arr):
    answer = [arr[x] for x in range(len(arr)) if arr[x:x+1] != arr[x+1:x+2]]
    return answer
