#https://school.programmers.co.kr/learn/courses/30/lessons/142086
#가장 가까운 같은 글자

def solution(s):
    answer = []
    temp = {}
    
    for idx, word in enumerate(s):
        if word not in temp:
            temp[word] = idx
            answer += [-1]
        else:
            answer += [idx - temp[word]]
            temp[word] = idx            
            
    return answer
