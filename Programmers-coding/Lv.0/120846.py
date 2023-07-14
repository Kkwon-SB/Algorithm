#https://school.programmers.co.kr/learn/courses/30/lessons/120846
#합성수 찾기

def solution(n):
    answer = 0
    cnt = 0
    
    for i in range(4, n+1):
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt >=3:
            answer += 1
        cnt = 0
    return answer
