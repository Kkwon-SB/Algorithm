#https://school.programmers.co.kr/learn/courses/30/lessons/12921
#소수 찾기

def solution(n):
    cnt =0 
    temp = [i for i in range(n+1)]
    
    for i in range(2, int(n**0.5)+1):
        if temp[i] == 0:
            continue
            
        for j in range(i+i, n+1, i):
            temp[j] = 0
            
    for i in temp:
        if i != 0:
            cnt += 1   
    
    return cnt-1 #1제외
