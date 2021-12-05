# 신입사원

# n이 최대 100,000이므로 sys사용
import sys
input = sys.stdin.readline

test_case = int(input())
for i in range(test_case):

    N = int(input())
    count = 1  # 한명은 무조건 통과
    rank = [0 for _ in range(N)]  # 0으로 인원만큼 초기화

    '''
      면접 순위만 비교하면 되므로, 성적이 오름차순으로 면접 순위를 입력받음
      ex) 1 3 -> 성적 1위 면접 3위 -> s[0] = 3
    '''
    for _ in range(1, N):
        resume, interview = map(int, input().split())
        rank[resume-1] = interview

    min = rank[0]  # 최솟값에 첫사람의 인터뷰순위를 넣음

    for i in range(1, N):
        if rank[i] < min:  # 최솟값이 더 클 경우 1을 증가
            count += 1
            min = rank[i]

    print(count)
