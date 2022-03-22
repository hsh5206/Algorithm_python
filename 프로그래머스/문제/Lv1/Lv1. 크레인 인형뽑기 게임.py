def solution(board, moves):
    stack = []
    result = 0
    for x in moves:
        for i in range(len(board)):
            target = board[i][x-1]
            if target != 0:
                board[i][x-1] = 0
                if stack and stack[-1] == target:
                    stack.pop()
                    result += 2
                else:
                    board[i][x-1] = 0
                    stack.append(target)
                break
    return result
