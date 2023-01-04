#이진 탐색, start, end 설정

#https://www.acmicpc.net/problem/1920
#수 찾기
a = input() 
num_list = list(map(int, input().split()))
b = input() 
find_list = list(map(int, input().split()))

num_list.sort()


for find_num in find_list:
    check = 0
    start = 0
    end = len(num_list)-1

    while start <= end:
        mid_idx = (start+end)//2 
        mid_num = num_list[mid_idx]

        if mid_num > find_num:#왼쪽으로
            end = mid_idx-1
        elif mid_num < find_num:#오른쪽으로
            start = mid_idx+1
        else:
            check = 1
            break

    if check == 1: print(1)
    else: print(0)
 
''' set.....사용할 수 있다는 것을 간과했다...
# 입력
N = int(input())
A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
M = int(input())
arr = list(map(int, input().split()))

for num in arr:				# arr의 각 원소별로 탐색
    print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력
'''
