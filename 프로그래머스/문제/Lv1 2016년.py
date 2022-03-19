month_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
             7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
weeks = {0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON', 4: 'TUE', 5: 'WED', 6: 'THU'}


def solution(a, b):
    period = 0
    for k in range(1, a):
        period += month_day[k]
    period += b
    return 'THU'if period % 7-1 == -1 else weeks[period % 7-1]
