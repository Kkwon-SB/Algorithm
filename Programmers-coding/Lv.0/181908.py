#https://school.programmers.co.kr/learn/courses/30/lessons/181908
#접미사인지 확인하기

def solution(my_string, is_suffix):
    
    if my_string[-len(is_suffix):] == is_suffix: return 1
    return 0

# def solution(my_string, is_suffix):
#     answer = []
#     hap = ''
    
#     my_string = my_string[::-1]

#     for i in my_string:
#         hap = i + hap
#         answer.append(hap)
    
#     if is_suffix in answer:
#         return 1
#     else:
#         return 0
