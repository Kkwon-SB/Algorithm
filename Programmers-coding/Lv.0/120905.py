#https://school.programmers.co.kr/learn/courses/30/lessons/120905
#n의 배수 고르기

def solution(n, numlist):
    answer = []
    
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    
    return answer


    # return [i for i in numlist if i % n == 0]
