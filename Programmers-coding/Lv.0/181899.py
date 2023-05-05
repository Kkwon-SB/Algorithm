#https://school.programmers.co.kr/learn/courses/30/lessons/181899
#카운트 다운

def solution(start, end):
    answer = []
    
    for i in range(start, end-1, -1):
        answer.append(i)
        
    return answer
