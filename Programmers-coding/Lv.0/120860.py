#https://school.programmers.co.kr/learn/courses/30/lessons/120860
#직사각형 넓이 구하기

def solution(dots):
    a, b = 0, 0
    
    while True:
        for i in range(len(dots)-1): #0~3
            if a == 0:
                a = dots[i][0] - dots[i+1][0]
            if b == 0:
                b = dots[i][1] - dots[i+1][1]
                
            if a != 0 and b != 0:
                return abs(a * b)
            
    
    return abs(a * b)
