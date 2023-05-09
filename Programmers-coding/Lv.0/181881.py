#https://school.programmers.co.kr/learn/courses/30/lessons/181881
#조건에 맞게 수열 변환하기 2

import copy

def solution(arr):
    next_arr = arr.copy()
    cnt = 0
    
    while True:
        for i in range(len(arr)):
            if next_arr[i] >= 50 and next_arr[i] % 2 == 0:
                next_arr[i] /= 2
                continue

            if next_arr[i] < 50 and next_arr[i] % 2 == 1:
                next_arr[i] = arr[i] * 2 + 1
                continue
                
        if arr == next_arr:
            break
        # new_lst = copy.deepcopy(lst)
        arr = copy.deepcopy(next_arr)
        cnt += 1 
        
    return cnt

#case2
# def solution(arr):
    
#     next_arr == arr
#     cnt = 0
    
#     while True:

#         for i in range(len(arr)):
#             if next_arr[i] >= 50 and next_arr[i] % 2 == 0:
#                 next_arr[i] /= 2
#                 continue

#             if next_arr[i] < 50 and next_arr[i] % 2 == 1:
#                 next_arr[i] = arr[i] * 2 + 1
#                 continue
        
#         if arr == next_arr:
#             break
#             # return cnt
#         else:
#             arr = next_arr
        
#         cnt += 1 
        
#     return cnt
