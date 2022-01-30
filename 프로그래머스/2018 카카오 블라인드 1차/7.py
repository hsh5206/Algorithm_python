# 추석 트랙픽
def solution(lines):
    start = []
    end = []
    for log in lines:
        time = log.split()
        start.append(get_start_second(time[1], time[2]))
        end.append(get_second(time[1]))

    answer = 0
    for i in range(len(end)):
        result = 0
        for j in range(i, len(start)):
            if end[i] + 1000 > start[j]:
                result += 1
        answer = max(answer, result)

    return answer


def get_second(time):
    temp, milisecond = time.split('.')
    hour, minute, second = map(int, temp.split(':'))
    milisecond = int(milisecond)
    return (hour*60**2+minute*60+second)*1000+milisecond


def get_start_second(time, duration):
    time_duration = duration.replace('s', '')
    temp = int(float(time_duration)*1000)
    return get_second(time) - temp + 1
