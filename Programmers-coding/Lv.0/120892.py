#https://school.programmers.co.kr/learn/courses/30/lessons/120892
#암호 해독

def solution(cipher, code):
    answer = ''
    
    for i in range(1, len(cipher)+1):
        if i % code == 0:
            answer += cipher[i-1]
    
    return answer

    #return cipher[code-1::code]
