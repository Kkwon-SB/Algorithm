#https://school.programmers.co.kr/learn/courses/30/lessons/181926

#1. for문으로 돌리면서 값에 따라 적용하는 방법
#2. count함수로 한번에 측정 후 적용

def solution(n, control):
    
    array = list(control)
    w_cnt = array.count('w') 
    s_cnt = array.count('s') * -1
    d_cnt = array.count('d') * 10
    a_cnt = array.count('a') * -10
    
    answer = n + w_cnt + s_cnt + d_cnt + a_cnt
    
    return answer
