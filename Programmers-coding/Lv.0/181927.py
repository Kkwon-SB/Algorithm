#마지막 두 원소  https://school.programmers.co.kr/learn/courses/30/lessons/181927

def solution(num_list):
    
    if num_list[-1] > num_list[-2]:
        new = num_list[-1] - num_list[-2]
        num_list.append(new)
    else:
        new = num_list[-1] * 2
        num_list.append(new)
        
    return num_list
