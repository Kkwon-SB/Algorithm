#https://school.programmers.co.kr/learn/courses/30/lessons/181878
#원하는 문자열 찾기

def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0


'''case2
    myString = myString.lower()
    pat = pat.lower()

    if pat.lower() in myString.lower():
        return 1
    else:
        return 0
'''

'''case2
     myString = myString.lower()
     pat = pat.lower()

     if pat in myString:
         return 1
     else:
         return 0
'''
