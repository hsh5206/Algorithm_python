# 성적이 낮은 순서로 학생 출력하기

n = int(input())
arr = []
for i in range(N):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

# 람다 표현식
arr = sorted(arr, key=lambda student: student[1])

for student in arr:
    print(student[0], end=' ')
