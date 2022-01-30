# 셔틀버스
def solution(n, t, m, timetable):
    crew_time = []
    for time in timetable:
        crew_time.append(get_time(time))
    crew_time.sort()

    bus_time = []
    for i in range(n):
        bus_time.append(get_bus_time(t, i))

    my_time = 0
    temp = 0
    for bus in bus_time:
        my_time = bus
        max_people = m
        for i in range(temp, len(crew_time)):
            if bus >= crew_time[i] and max_people:
                max_people -= 1
                temp += 1
                if max_people == 0:
                    my_time = crew_time[i] - 1

    answer = change_time(my_time)
    return answer


def get_time(time):
    hour = int(time[:2]) * 60
    minute = int(time[3:])
    return hour + minute


def get_bus_time(t, i):
    hour = 9*60
    return hour+t*i


def change_time(time):
    hour = str(time // 60)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(time % 60)
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute
