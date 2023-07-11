#https://school.programmers.co.kr/learn/courses/30/lessons/120824
#짝수 홀수 개수

def solution(num_list):
    even, odd = 0, 0
    for i in num_list:
        if i % 2 == 0: #짝
            even += 1
        else:
            odd += 1 
    
    return even, odd
