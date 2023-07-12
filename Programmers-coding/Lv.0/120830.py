#https://school.programmers.co.kr/learn/courses/30/lessons/120830
#양꼬치

def solution(n, k):
    a = n * 12000
    b = 2000 * (k - (n // 10))
    b = b if b > 0 else 0
    
    return a + b
