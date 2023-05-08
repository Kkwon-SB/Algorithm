#https://school.programmers.co.kr/learn/courses/30/lessons/181887
#홀수 vs 짝수


def solution(num_list):
    case1, case2 = 0, 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            case1 += num_list[i]
        else:
            case2 += num_list[i]
    
    return max(case1, case2)
