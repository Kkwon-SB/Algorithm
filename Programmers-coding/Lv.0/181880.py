#https://school.programmers.co.kr/learn/courses/30/lessons/181880
#1로 만들기

def solution(num_list):
    
    cnt = 0
    for i in num_list:
        num = i
        
        while num != 1:
            cnt += 1
            
            if num % 2 == 0:
                num /= 2
            else:
                num = (num-1) /2
    
    return cnt
