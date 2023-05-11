#https://school.programmers.co.kr/learn/courses/30/lessons/181865
#간단한 식 계산하기

def solution(binomial):
    a, b, c = binomial.split()
    if b == '+':
        return int(a) + int(c)
    if b == '-':
        return int(a) - int(c)
    if b == '*':
        return int(a) * int(c)
    
    # return eval(binomial)
