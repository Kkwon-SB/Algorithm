#https://school.programmers.co.kr/learn/courses/30/lessons/12932
#자연수 뒤집어 배열로 만들기

def solution(n):
    '''
    a = list(map(int, str(n)))
    a.reverse()
    
    return a    
    '''
    
    n = sorted(list(str(n)), reverse=True)
    answer = [int(i) for i in n]
    return answer
