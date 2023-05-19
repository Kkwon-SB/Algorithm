#https://school.programmers.co.kr/learn/courses/30/lessons/181837
#커피 심부름

def solution(order):
    answer = 0
    
    for i in order:
        if 'latte' in i:
            answer+= 5000    
        else:
            answer+= 4500

    return answer
