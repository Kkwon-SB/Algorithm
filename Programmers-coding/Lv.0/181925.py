#https://school.programmers.co.kr/learn/courses/30/lessons/181925
#수 조작하기 2

#sum변수를 만들어서 새롭게 들어오는 값이랑 차이를 구해 문자 추측
def solution(numLog):
    answer = []
    sum = numLog[0]
    
    for i in range(1, len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            answer.append('w')
        elif numLog[i] - numLog[i-1] == -1:
            answer.append('s')
        elif numLog[i] - numLog[i-1] == 10:
            answer.append('d')
        elif numLog[i] - numLog[i-1] == -10:
            answer.append('a')

    return ''.join(answer)
