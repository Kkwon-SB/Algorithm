#https://school.programmers.co.kr/learn/courses/30/lessons/181909
#접미사 배열

def solution(my_string):
    answer = []
    hap = ''
    
    my_string = my_string[::-1]

    for i in my_string:
        hap = i + hap
        answer.append(hap)
    
    answer.sort()
    return answer
