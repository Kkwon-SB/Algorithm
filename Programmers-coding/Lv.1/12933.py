#https://school.programmers.co.kr/learn/courses/30/lessons/12933
#정수 내림차순으로 배치하기

def solution(n):
    
    answer = sorted(str(n), reverse=True) 
    #문자열을 리스트로 감쌀 필요 없음, sortd 결과로 리스트로 반환됨  list(str(n))
    
    return int(''.join(answer))
    
