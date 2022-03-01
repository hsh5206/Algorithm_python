# 기능개발
def solution(progresses, speeds):
    days = []
    for program, speed in zip(progresses, speeds):
        temp = (100-program) % speed
        days.append((100-program)//speed + 1 if temp else (100-program)//speed)

    answer = []
    count = 1
    start = days[0]
    for i, x in enumerate(days):
        if i+1 < len(days) and start >= days[i+1]:
            count += 1
        else:
            answer.append(count)
            if i + 1 < len(days):
                start = days[i+1]
            count = 1

    return answer
