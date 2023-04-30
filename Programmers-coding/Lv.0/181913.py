#https://school.programmers.co.kr/learn/courses/30/lessons/181913
#문자열 여러 번 뒤집기

def solution(my_string, queries):
    my_string = list(my_string)
    for s, e in queries:        
        my_string[s:e+1] = my_string[s:e+1][::-1]
        
    return ''.join(my_string)
'''
def solution(my_string, queries):
    for s, e in queries:
        temp = my_string[s:e+1][::-1]
        my_string = my_string[:s] + temp + my_string[e+1:]
        
    return my_string
'''


'''
def solution(my_string, queries):
    #for query in queries:
    for s, e in queries:
        # s, e = query[0], query[1]
        temp = my_string[s:e+1][::-1]
        # temp = temp[::-1]
        my_string = my_string[:s] + temp + my_string[e+1:]
        
    return my_string
'''
