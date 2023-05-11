#https://school.programmers.co.kr/learn/courses/30/lessons/181872
#특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

def solution(myString, pat):
    x = myString[::-1].index(pat[::-1])
    return myString[:len(myString)-x]
