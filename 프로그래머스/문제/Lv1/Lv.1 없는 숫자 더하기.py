def solution(numbers):
    numbers = set([i for i in range(10)]) - set(numbers)
    return sum(numbers)
