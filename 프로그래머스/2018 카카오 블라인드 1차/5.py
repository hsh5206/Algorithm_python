# 뉴스 클러스터링
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    one = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    two = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    print(one)
    print(two)

    one_and_two = set(one) & set(two)
    one_or_two = set(one) | set(two)

    and_num = 0
    or_num = 0
    for i in one_and_two:
        and_num += min(one.count(i), two.count(i))
    for i in one_or_two:
        or_num += max(one.count(i), two.count(i))

    if or_num == 0:
        return 65536
    else:
        return int(and_num / or_num * 65536)
