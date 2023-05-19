#https://school.programmers.co.kr/learn/courses/30/lessons/181834
#l로 만들기

def solution(myString):
    myString = list(myString)
    for i in range(len(myString)):
        if ord(myString[i]) < 108: #ord('l') >>> 108
            myString[i] = 'l'
    
    return ''.join(myString)
