#https://school.programmers.co.kr/learn/courses/30/lessons/120816
#피자 나눠 먹기 (3)

def solution(slice, n):
    mok, rest = divmod(n , slice)
    return mok + (1 if rest > 0 else 0) 
