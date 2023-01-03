'''
인덱스와 값을 사용해야 답에 접근할 수 있다고 생각, -> enumerate사용, 만약 enumerate사용하게된다면 이중 for문을 작성해야 하는 상황 -> 비효율,  
'''

#https://www.acmicpc.net/problem/11003
#최솟값 찾기

from collections import deque

num_case , std = map(int, input().split())
test_box = deque()
num_list = list(map(int, input().split()))

for i in range(num_case):
    while test_box and test_box[-1][1] > num_list[i]: #test_box에 값이 들어있고, 마지막이 현재 값보다 클 때 -> 삭제
        test_box.pop()
    test_box.append((i, num_list[i]))

    if test_box[0][0] <= i- std:
        test_box.popleft()
    print(test_box[0][1], end=' ')


'''#첫 시도
#요소가 2가지 경우 앞에 요소를 기준으로 비교
from collections import deque

num_case , std = 12, 3
num_list = [1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]

# std_list = [num_list[0]+1] * std-1 #기준 값 만큼 앞에 추가
# num_list =  std_list + num_list

test_box = deque()

answer = []
       
for idx , i in enumerate(num_list):
    test_box.append((idx , i))
    if test_box[-1][1]

    if test_box[-2][1] <  test_box[-1][1]: # 2,  6
'''
