# https://school.programmers.co.kr/learn/courses/30/lessons/64061
#64061
# Type1. 55분 소요 -> 'time error'
"""
def solution(board, moves):
    real_answer = 0
    result = []
    answer = []
    i = 0

    while i != 5:
        answer2 = []

        for line in board:
            if line[i] != 0:
                answer2.append(line[i])
        i += 1
        answer.append(answer2)

    for i in moves:
        if len(answer[i-1]) != 0:
            result.append(answer[i-1][0])
            del answer[i-1][0]

        if len(result) < 2:
            continue

        if result[-1] == result[-2]:
            result = result[:-2]
            real_answer += 2

    return (real_answer)
"""

# Type2. 12분 소요 -> (정답)


def solution(board, moves):
    answer = []
    cnt = 0
    for c in moves:
        i = 0

        while board[i][c-1] == 0:
            i += 1
            if i == len(board):
                break
        else:
            answer.append(board[i][c-1])
            board[i][c-1] = 0

        if len(answer) < 2:
            continue

        if answer[-1] == answer[-2]:
            answer = answer[:-2]
            cnt += 2

    return (cnt)


"""
처음 접근 했던 방식은 주어진 행 기준의 board의 배열을 열(column) 기준으로 바꿔 접근하는것이였다.
행 형태를 열 형태로 바꿀 수만 있다면 쉽게 문제 풀이를 할 수 있을것이라 생각했지만 생각보다 구현 코드가 너무 복잡해졌고 'time error'발생시켰다.
그래서 2번째 방법에서는 주어진 값 그대로 두고 인덱스를 통해 원하는 위치에 접근했다. 오히려 복잡할거라고 예상했던 방법이 짧은 시간에 쉽게 풀렸다. 
Type1형태로 풀면서 전체적인 문제 접근 방식을 파악한것 같다
덕분에 Type2형태에서는 단 12분 만에 문제를 풀 수 있었다.\

=> 전체적인 흐름을 '미리' 파악하고 효율적인 방법을 생각해내야한다.
진행 도중 코드 전체를 변경하게 되면 시간을 너무 많이 잡아먹는다. 
"""
