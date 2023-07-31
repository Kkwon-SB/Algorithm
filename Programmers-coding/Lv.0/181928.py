#https://school.programmers.co.kr/learn/courses/30/lessons/181928
#이어 붙인 수

def solution(num_list):
    
    odd = ''
    even = ''
    
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
            
    answer = int(odd) + int(even)
    return answer
