#https://school.programmers.co.kr/learn/courses/30/lessons/77884
#약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    cnt = 0
    
    for num in range(left, right+1):
        for i in range(1, num+1):
            if num % i == 0:#약수
                cnt += 1
                
        if cnt % 2 == 0:
            answer += num
        else:
            answer -= num
            
        cnt = 0
        
    return answer
