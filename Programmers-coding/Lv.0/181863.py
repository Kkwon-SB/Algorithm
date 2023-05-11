#https://school.programmers.co.kr/learn/courses/30/lessons/181863
#rny_string

def solution(rny_string):
    return rny_string.replace('m', 'rn')
'''    
    rny_string = list(rny_string)
    
    for i in range(len(rny_string)):
        if rny_string[i] == 'm':
            rny_string[i] = 'rn'

    return ''.join(rny_string)
'''
