#https://school.programmers.co.kr/learn/courses/30/lessons/120852
#소인수분해

def solution(n):
    answer = []
    
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = n // i
                answer.append(i)
                break
            
    a = sorted(list(set(answer))) #set 사용 시, 정렬이 없어지기 때문에 주의!
    return a
