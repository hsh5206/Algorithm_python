# 오픈채팅방
uuid = dict()
id_name = dict()


def solution(record):
    answer = []
    i = 0
    for str in record:
        if str.split()[0] == 'Leave':
            type, id = str.split()
            name = id_name[id]
            answer.append([name, '님이 나갔습니다.'])
            uuid[id].append(i)
            i += 1
        else:
            type, id, name = str.split()
            id_name[id] = name
            if type == 'Enter':
                if uuid.get(id):
                    id_name[id] = name
                    change(id, name, answer)
                    uuid[id].append(i)
                else:
                    uuid[id] = [i]
                answer.append([name, '님이 들어왔습니다.'])
                i += 1
            else:
                change(id, name, answer)
                id_name[id] = name
                # 닉네임 바꿈
    result = []
    for x in answer:
        result.append(x[0]+x[1])
    return result


def change(id, name, answer):
    for x in uuid[id]:
        answer[x][0] = name


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
      "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
