#https://school.programmers.co.kr/learn/courses/30/lessons/120907
#OX퀴즈

def solution(quiz):
    answer = []
    
    for i in quiz:
        temp = i.split()
        
        if eval(temp[0]+temp[1]+temp[2]) == int(temp[-1]):
            answer.append('O')
        else:
            answer.append('X')
        
    return answer
