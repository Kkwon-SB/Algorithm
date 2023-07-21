#https://school.programmers.co.kr/learn/courses/30/lessons/120912
#7의 개수

def solution(array):
    return str(array).count('7')

'''
    array = ''.join([str(i) for i in array])
    
    cnt = 0
    
    for i in array:
        if i == '7':
            cnt += 1
    
    return cnt
'''
