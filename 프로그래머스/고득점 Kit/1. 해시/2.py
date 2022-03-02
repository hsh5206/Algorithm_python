# 전화번호 목록
def solution(phone_book):
    dictionary = dict()
    for number in phone_book:
        for i in range(1, len(number)+1):
            x = number[:i]
            if dictionary.get(x):
                if i == len(number):
                    return False
                if dictionary[x] == 2:
                    return False
            else:
                dictionary[x] = 1
                if i == len(number):
                    dictionary[x] = 2
    return True
