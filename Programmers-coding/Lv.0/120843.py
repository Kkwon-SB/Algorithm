#https://school.programmers.co.kr/learn/courses/30/lessons/120843
#공 던지기

def solution(numbers, k):
    cnt = 1
    idx = 0
    
    while cnt <= k:
        target = numbers[idx]
        cnt += 1
        idx += 2
        
        if idx >= len(numbers):
            idx = idx % len(numbers)
            
    return target
