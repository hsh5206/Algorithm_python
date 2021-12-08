# 실수형 0 생략
import sys
a = 5.  # 5.0
print(a)
a = -.7  # -0.7
print(a)

# INF - 지수표현방식 -> 실수형
a = 1e9  # 10억
print(a)

# 실수정보의 정확도 오차발생 -> round()함수 이용
a = 0.3 + 0.6  # 0.8999999999999999
print(a)
print(round(a, 2))

# 나누기는 실수로
a = 7/3
print(a)

# 몫연산자
a = 7//3
print(a)

# n제곱
a = 2 ** 4
print(a)

# 리스트 []
# 1.인덱싱
#    0  1  2  3  4
#   -5 -4 -3 -2 -1
a = [3, 5, 4, 3, 2]
print(a[-5])
n = 6
# 2. 리스트 초기화
a = [0] * n
print(a)
# 3. 슬라이싱
a = [3, 5, 4, 3, 2]
print(a[2:5])
# 4. 컴프리헨션
a = [i for i in range(10)]
print(a)
# 컴프리헨션 - if문 가능
a = [i for i in range(20) if i % 2 == 1]
print(a)
# 컴프리헨션 - 2차원 리스트 초기화 (nXm배열 0으로 초기화)
n = 3
m = 4
a = [[0] * m for _ in range(n)]
print(a)
# 5. 리스트 메서드
a = [1, 2, 3, 4, 5]
print(a)
a.append(6)
print(a)
a.sort(reverse=True)
print(a)
a.sort()
print(a)
a.insert(3, 6)
print(a)
print(a.count(6))
a.remove(6)  # 앞에서 하나만 제거
print(a)
# remove 메소드 활용 - 모든 값 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
print(a)
result = [i for i in a if i not in remove_set]
print(result)

# 튜플 - 수정불가 ()
a = (1, 2, 3, 4, 5, 6, 7)
print(a)

# 사전(딕셔너리) - 키와 값 {키:값}
data = dict()
data['사과'] = 'APPLE'
data['바나나'] = 'BANANA'
data['코코넛'] = 'COCONUT'
print(data)
data = {
    '사과': 'Apple',
    '바나나': 'Banana',
    '코코넛': 'Coconut'
}
print(data)
if '사과' in data:
    print("'사과'키워드가 존재함")
key_list = data.keys()
print(key_list)
key_list = list(data.keys())
print(key_list)
value_list = data.values()
print(value_list)
value_list = list(data.values())
print(value_list)

# 집합(세트) {} - 합집합,교집합,차집합 기능 / 순서X
data = set([1, 1, 2, 3, 4, 4, 5])
data = {1, 1, 2, 3, 4, 4, 5}
print(data)
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a, b)
print(a | b)  # 합집합
print(a & b)  # 교집합
print(a-b)  # 차집합
# 추가함수
print(data)
data.add(6)
print(data)
data.update([5, 6, 7, 8])
print(data)
data.remove(3)
print(data)

# 입출력
# 입력을 위한 전형적인 소스코드
n = int(input())
data = list(map(int, input().split()))  # 한줄을 공백기준 인트화 리스트화
print(data)
data.sort(reverse=True)
print(data)
a, b, c = map(int, input().split())  # 3개의 데이터 입력받음
print(a, b, c)
data = sys.stdin.readline().rstrip()  # 빠르게 한줄을 입력받음(rstrip은 엔터때문에)
# 출력을 위한 전형적인 소스코드
result = 7
print(f"결과는 {result}입니다.")  # f-string문법

# 조건문 - 들여쓰기로 블록 지정
score = 85
if score >= 90:
    print("남성학우는 A입니다")
    if(score == 100):
        print("만점입니다.")
elif score >= 80:
    print("B")
else:
    print("C")
    print("최하등급입니다.")
# 논리연산자 -> and,or,not
# 기타연산자 -> in,not in
# pass키워드 - 아무일도 일어나지 않음
score = 85
if score >= 80:
    pass
else:
    print('성적이 80미만')
# 조건부표현식 - 한줄에 표현
score = 85
result = "Success" if score >= 80 else "Fail"

# 반복문
# while문
i = 1
result = 0
while i <= 9:
    result += i
    i += 1
print(result)
# for문
result = 0
for i in range(0, 10):  # range함수 -> range(시작 값, 끝 값 + 1)
    result += i
    i += 1
print(result)
# 리스트와 for문
array = [1, 2, 3, 4, 5]
for x in array:
    print(x)
# continue키워드와 break키워드


# 함수


def add(a, b):
    return a+b


x = 3
y = 4
result = add(x, y)
print(result)
# global키워드 - '바깥의 전역변수를 사용하겠다'
PI = 3.14


def getCircle(x):
    global PI
    return x*x*PI


print(getCircle(3))

# 패킹&언패킹 - 여러 반환값을 패킹해서 리턴, 여러값을 언패킹해서 변수에 각각 할당


def operator(a, b):
    add = a+b
    subtract = a-b
    multiply = a*b
    divide = a/b
    return add, subtract, multiply, divide


a, b, c, d = operator(7, 3)
print(a, b, c, d)

# 람다표현식
# 1
print((lambda a, b: a+b)(3, 7))
# 2
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(array)
print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[0]))
# 3
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))


# 코딩테스트에 필요한 필수 라이브러리
# 1. 내장함수
# sum() -> 합
result = sum([1, 2, 3, 4, 5])
print(result)
# min(), max() -> 최대값 최소값
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
# eval() -> 문자열 수학수식의 값을 반환
result = eval("(3+5)*7")
print(result)
# sorted() -> 정렬
result = sorted([9, 1, 8, 5, 4])
print(result)
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1])
print(result)
# 2. itertools
# permutations & product
# combinations & combinations_with_replacement
# 3. heapq
# 4. bisect
# 5. collections
# Counter
# 6. math
# gcd & lcm

# 기타팁
# 스왑기능
a, b = 3, 6
print(a, b)
a, b = b, a
print(a, b)
