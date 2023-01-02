#코드 뿐만 아니라 받아오는 값도 시간을 절약할 수 있는 방법으로 받아오는 방법을 생각하게 되었다.

import sys

input = sys.stdin.readline

data_num, q_num = map(int, input().split())
num_list = list(map(int, input().split()))

s = [0]
temp = 0
for i in num_list:
    temp += i
    s.append(temp)

for _ in range(q_num):
    a, b  = map(int,sys.stdin.readline().split())
    print(s[b] - s[a-1])

'''
#초기 작성 코드 - 풀이는 맞았지만 시간초과 문제

data_num, q_num = map(int, input().split())

num_list = list(map(int, input().split()))

s = [0]
temp = 0

for i in num_list:
    temp += i
    s.append(temp)

for _ in range(q_num):
    a, b  = map(int, input().split())

    print(s[b] - s[a-1])
'''
