#https://school.programmers.co.kr/learn/courses/30/lessons/12982
#예산

def solution(d, budget):
    
    a = d.sort()
    return a
    total = 0
    cnt = 0
    
    for i in d:
        total += i
        
        if total <= budget:
            cnt += 1
        else:
            return cnt
    
    return cnt
