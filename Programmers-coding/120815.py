#https://school.programmers.co.kr/learn/courses/30/lessons/120815
#

#최소공배수
def solution(n):
    v = 6 * n
    a = 6
    
    while n > 0:
        a, n = n, a % n
    
    return (v / a) // 6
