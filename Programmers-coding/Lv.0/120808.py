#https://school.programmers.co.kr/learn/courses/30/lessons/
#분수의 덧셈

def solution(numer1, denom1, numer2, denom2):
    mom = LCM(denom1, denom2) #최소공배수 함수호출
    son = (mom // denom1 * numer1) + (mom // denom2 * numer2)
    
    while True:#기약분수 만들기
        a, b = son, mom
        while b:
            a, b = b, a % b
        son //=a
        mom //=a
        if a == 1:#1이면 기약분수
            break
        
    return [son, mom]
  
def LCM(denom1, denom2):#최소공배수
    a, b = denom1, denom2
    while b:
        a, b = b, a % b
    return denom1*denom2//a
