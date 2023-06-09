#https://school.programmers.co.kr/learn/courses/30/lessons/86051
#없는 숫자 더하기

def solution(numbers):
    return 45 - sum(numbers)
'''
def solution(numbers):
    answer = 0
    
    for i in range(10):
        if numbers.count(i) == 0:
            answer += i
    return answer

'''
'''
def solution(numbers):
    temp = [i for i in range(10)]
    numbers.sort()
    numbers += [0] * (10 - len(numbers))
    answer, i, j = 0, 0, 0
    
    while j < len(temp):
        if numbers[i] != temp[j]:
            answer += temp[j]
            j += 1
        else:
            i += 1
            j += 1
        
    return answer
'''
