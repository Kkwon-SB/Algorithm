#https://school.programmers.co.kr/learn/courses/30/lessons/181879
#길이에 따른 연산

def solution(num_list):
    answer = 1
    
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        # for i in num_list:
        #     answer *= i
        answer = [answer *= i for i in num_list]

    return answer
