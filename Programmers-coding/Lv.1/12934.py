#https://school.programmers.co.kr/learn/courses/30/lessons/12934
#정수 제곱근 판별

def solution(n):
    
    a = int(n ** 0.5)
    
    if a * a == n: #제곱ㅇ 
        return (a+1)**2
    else:
        return -1
    
