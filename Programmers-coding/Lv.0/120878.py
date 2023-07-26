#https://school.programmers.co.kr/learn/courses/30/lessons/120878
#유한소수 판별하기

from math import gcd

def solution(a, b):
    a, b = check1(a, b)
    return check2(b)


def check1(a, b):
    # b //= gcd(a,b)
    for i in range(a, 1, -1):
        if a%i==0 and b%i==0:
            a//=i
            b//=i
    return a, b

def check2(b):
    while b != 1:
        if b % 2 == 0:
            b//=2
            continue
        if b % 5 == 0:
            b//=5
        else:
            return 2
    return 1


    
