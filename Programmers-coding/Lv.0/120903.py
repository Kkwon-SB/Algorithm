#https://school.programmers.co.kr/learn/courses/30/lessons/120903
#배열의 유사도

def solution(s1, s2):
                 
    return len(set(s1) & set(s2))
