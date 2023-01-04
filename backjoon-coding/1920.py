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
