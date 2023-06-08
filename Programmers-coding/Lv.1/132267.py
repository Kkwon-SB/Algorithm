#https://school.programmers.co.kr/learn/courses/30/lessons/132267
#콜라 문제

def solution(a, b, n):
    new = n
    answer = 0
    
    while new != 0:
        new, rest = divmod(new, a)
        new *= b 
        answer += new
        
        if new + rest < a:
            return answer
        else:
            new += rest
