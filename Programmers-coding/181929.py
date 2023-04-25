#https://school.programmers.co.kr/learn/courses/30/lessons/181929

def solution(num_list):
    
    mul = 1
    sqr = 0
    
    for i in num_list:
        mul *= i
        sqr += i
        
    sqr *= sqr 
        
    if mul > sqr:
        return 0
    else:
        return 1
