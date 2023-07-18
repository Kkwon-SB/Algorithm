#https://school.programmers.co.kr/learn/courses/30/lessons/120897
#약수 구하기

def solution(n):
    return [i for i in range(1, n+1) if n % i == 0]


'''
    answer = [1]
    
    for i in range(2, n+1):
        if n % i == 0:
            answer.append(i)
    
    return answer

'''
