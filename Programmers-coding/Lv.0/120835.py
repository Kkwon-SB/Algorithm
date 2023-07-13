#https://school.programmers.co.kr/learn/courses/30/lessons/120835
#진료 순서 정하기

def solution(emergency):
    temp = sorted(emergency, reverse=True)
    num_dict = {}

    for i in range(len(emergency)):
        num_dict[str(temp[i])] = i+1
    
    return [num_dict[str(i)] for i in emergency]
