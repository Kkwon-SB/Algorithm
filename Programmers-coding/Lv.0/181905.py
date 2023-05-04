#https://school.programmers.co.kr/learn/courses/30/lessons/181905
#문자열 뒤집기

def solution(my_string, s, e):
    
    # target = my_string[s:e+1][::-1]
    # return my_string[:s] + target + my_string[e+1:]
    
    my_string[s:e+1] = my_string[s:e+1][::-1]
    return my_string
