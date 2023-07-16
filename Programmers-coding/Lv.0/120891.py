#https://school.programmers.co.kr/learn/courses/30/lessons/120891
#369게임

def solution(order):

    order = str(order)

    return len([i for i in order if i in ['3','6','9']]) 

'''
    for i in order:
        if i in ['3','6','9']:
            cnt += 1
'''
