#https://school.programmers.co.kr/learn/courses/30/lessons/181871
#문자열이 몇 번 등장하는지 세기

def solution(myString, pat):
    cnt = 0
    
    for i in range(0, len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            cnt += 1
    
    return cnt
