#https://school.programmers.co.kr/learn/courses/30/lessons/1845
#폰켓몬

def solution(nums):
    half_len = len(nums) // 2
    
    nums = list(set(nums))
    
    if len(nums) > half_len:
        return half_len
    else:
        return len(nums)

# from itertools import combinations

# def solution(nums):
#     nums.sort()
#     aa = combinations(nums,len(nums)//2)
    
#     answer = []
    
#     for i in aa:
#         answer.append(i)
    
#     result = list(set(map(tuple, answer)))
#     result = [list(x) for x in result]
    
#     return (result)
