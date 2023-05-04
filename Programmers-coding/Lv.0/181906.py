#https://school.programmers.co.kr/learn/courses/30/lessons/181906
#접두사인지 확인하기

def solution(my_string, is_prefix):
    
     if is_prefix == my_string[:len(is_prefix)]:
         return 1
     else:
         return 0
    #return 1 if is_prefix == my_string[:len(is_prefix)] else 0
