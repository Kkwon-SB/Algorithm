#https://school.programmers.co.kr/learn/courses/30/lessons/181903
#qr code

def solution(q, r, code):
    answer = ''
    
    for i in range(len(code)):
        if i % q == r:
            answer += code[i]
    return answer
