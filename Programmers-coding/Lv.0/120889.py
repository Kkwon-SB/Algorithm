#https://school.programmers.co.kr/learn/courses/30/lessons/120889
#삼각형의 완성조건 (1)

def solution(sides):
    return 1 if max(sides) < sum(sides) - max(sides) else 2
