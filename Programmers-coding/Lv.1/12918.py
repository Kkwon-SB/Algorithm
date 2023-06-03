#https://school.programmers.co.kr/learn/courses/30/lessons/12918
#문자열 다루기 기본

def solution(s):
    try:
        int(s)
        
        if len(s) == 4 or len(s) == 6: #길이가 4 or 6
            return True
        else:
            return False
    except:
        return False
    
    
'''
    #5, 6, 28, 29
    for i in s:
        if ord(i) > 57: # 0 ~ 9 = 48 ~ 57
            return False
    return True
'''
'''
    # #28 29 실패
    for i in s:
        if i.isalpha():
            return False
    return True
'''
