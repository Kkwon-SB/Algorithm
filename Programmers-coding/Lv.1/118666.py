#https://school.programmers.co.kr/learn/courses/30/lessons/118666
#성격유형검사
 
score_board = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
name_board = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0, }
names = ['R', 'T', 'C', 'F', 'J','M','A', 'N']
pre_answer = []

def solution(survey, choices):
    answer = ''

    for a, b in zip(survey, choices):
        if b > 4:
            name_board[a[1]] += score_board[b]
        elif b < 4:
            name_board[a[0]] += score_board[b]
        else:
            pass
    
    for i in name_board: 
        pre_answer.append(name_board.get(i))

    for i in range(0,8,2):
        if pre_answer[i] > pre_answer[i+1]:
            answer += names[i]
        elif pre_answer[i] < pre_answer[i+1]:
            answer += names[i+1]
        else:
            answer += names[i]
       
    return answer


