# 파일명 정렬
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def solution(files):
    arr = [['' for _ in range(3)] for _ in range(len(files))]
    for file in range(len(files)):
        do = False
        slice = 0
        for x in range(len(files[file])):
            if files[file][x] in number:
                if not do:
                    arr[file][0] = files[file][:x]
                    slice = x
                    do = True
                    if x == len(files[file])-1:
                        arr[file][1] = files[file][x:]
            if x == len(files[file])-1:
                arr[file][1] = files[file][slice:]
            if files[file][x] not in number:
                if do:
                    arr[file][1] = files[file][slice:x]
                    arr[file][2] = files[file][x:]
                    break
    arr.sort(key=lambda x: (x[0].lower(), int(x[1])))

    answer = []
    for i in range(len(arr)):
        answer.append(arr[i][0]+arr[i][1]+arr[i][2])
    return answer


print(solution(["F-5", "B-50",
      "A-10", "F-14"]))
