import re


def solution(logs):
    answer = len(logs)
    for x in logs:
        now = re.findall(
            r'^[a-z_]+ : ', x)
        temp = re.findall(r' : [a-zA-Z]{1,}', x)
        print(now, temp)
        for i in range(len(now)):
            if now[i] != temp[i]:
                answer -= 1
                break
    return answer


print(solution(["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!",
      "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]))
