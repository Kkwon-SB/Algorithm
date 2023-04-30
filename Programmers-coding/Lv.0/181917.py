#https://school.programmers.co.kr/learn/courses/30/lessons/181917
#간단한 논리 연산

def solution(x1, x2, x3, x4):     
    if x1 != x2 or x1 == True and x2 == True:
        case1 = True
    else:
        case1 = False
        
    if x3 != x4 or x3 == True and x4 == True:
        case2 = True
    else:
        case2 = False

    if case1 != case2 or case1 == False and case2 == False:
        return False
    else:
        return True
        
