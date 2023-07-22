#https://school.programmers.co.kr/learn/courses/30/lessons/120861
#캐릭터의 좌표

def solution(keyinput, board):
    answer = [0,0]
    
    for way in keyinput:
        if way == 'left' and (board[0]-1)// 2 * -1 < answer[0]:
            answer[0] -= 1
    
        elif way == 'right' and (board[0]-1) // 2 > answer[0]:
            answer[0] += 1
            
        elif way == 'up' and (board[1]-1) // 2 > answer[1]:
            answer[1] += 1
            
        elif way == 'down' and (board[1]-1) // 2 * -1 < answer[1]:
            answer[1] -= 1
    
    return answer
