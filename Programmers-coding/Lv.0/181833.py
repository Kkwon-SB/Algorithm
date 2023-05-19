#https://school.programmers.co.kr/learn/courses/30/lessons/181833
#특별한 이차원 배열 1

def solution(n):
    answer = [[0]*n for _ in range(n)] 
    
    for i in range(n):
        answer[i][i] = 1
    
    return answer
