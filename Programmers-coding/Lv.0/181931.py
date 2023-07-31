#https://school.programmers.co.kr/learn/courses/30/lessons/181931
#등차수열의 특정한 항만 더하기

def solution(a, d, included):
    sum = a
    result = 0
    
    for i in range(len(included)):
    
        if included[i] == True:
            result += sum
        
        sum += d
            
            
    return result
    
    


# 방법2
# def solution(a, d, included):
#     sum = a
#     result = [sum]
#     answer = 0
    
#     for i in range(len(included)-1):
#         sum += d
#         result.append(sum)
    
#     for j in range(len(included)):
#         if included[j] == True:
#             answer += result[j]
        
#     return answer
