#https://school.programmers.co.kr/learn/courses/30/lessons/120826
#특정 문자 제거하기

def solution(my_string, letter):
    
    return ''.join(i for i in my_string if i != letter)
    return my_string.replace(letter, '')
