#https://www.acmicpc.net/problem/11659
#구간합구하기4

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
