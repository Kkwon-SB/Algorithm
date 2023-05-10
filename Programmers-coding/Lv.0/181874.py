#https://school.programmers.co.kr/learn/courses/30/lessons/181874
#A 강조하기

def solution(myString):
    return myString.lower().replace('a', 'A')

'''
def solution(myString):
    myString = myString.lower()
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'a':
            myString[i] = 'A'
        
    return ''.join(myString)
'''
