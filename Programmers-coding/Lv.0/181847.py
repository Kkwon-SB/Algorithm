#https://school.programmers.co.kr/learn/courses/30/lessons/181847
#0 떼기

def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != '0':
            return n_str[i:]
