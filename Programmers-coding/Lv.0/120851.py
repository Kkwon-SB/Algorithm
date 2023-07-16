#https://school.programmers.co.kr/learn/courses/30/lessons/120851
#숨어있는 숫자의 덧셈 (1)

def solution(my_string):
    return sum([int(i) for i in my_string if not i.isalpha()])
