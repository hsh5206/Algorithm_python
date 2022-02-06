# 방금그곡
sound = {'A#': '1', 'C#': '2', 'D#': '3', 'F#': '4', 'G#': '5'}


def solution(m, musicinfos):
    answer = ''
    result = []

    m = m.replace('A#', sound['A#'])
    m = m.replace('C#', sound['C#'])
    m = m.replace('D#', sound['D#'])
    m = m.replace('F#', sound['F#'])
    m = m.replace('G#', sound['G#'])

    for music in musicinfos:
        title, time, melody = music_melody(m, music)
        if m in melody:
            result.append([title, time])
    result.sort(key=lambda x: -x[1])
    if result:
        answer = result[0][0]
    else:
        answer = '(None)'
    return answer


def music_melody(m, music):
    start, end, title, melody = music.split(',')
    start_hour, start_minute = map(int, start.split(':'))
    end_hour, end_minute = map(int, end.split(':'))

    hour = end_hour - start_hour
    minute = end_minute - start_minute
    time = hour*60 + minute

    melody = melody.replace('A#', sound['A#'])
    melody = melody.replace('C#', sound['C#'])
    melody = melody.replace('D#', sound['D#'])
    melody = melody.replace('F#', sound['F#'])
    melody = melody.replace('G#', sound['G#'])

    if time > len(melody):
        temp = time // len(melody)
        temp2 = time % len(melody)
        for _ in range(temp-1):
            melody += melody
            if len(melody) > len(m):
                break
        melody += melody[:temp2]
    else:
        temp2 = time % len(melody)
        melody = melody[:temp2]

    return title, time, melody


print(
    solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
