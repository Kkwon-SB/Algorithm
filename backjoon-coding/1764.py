#듣보잡 https://www.acmicpc.net/problem/1764
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_list = []
m_list = []

for _ in range(n):
    n_list.append(input())

for _ in range(m):
    m_list.append(input())

answer = list(set(n_list) & set(m_list))
answer.sort()

print(len(answer))
print(''.join(answer), end = '')


#시간초과 나오는데 이유를 모르겠다..
'''시도2
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

n_list = [0] * n
answer =[]

for i in range(n):
    n_list[i] = input()

for _ in range(m):
    mm = input()
    if mm in n_list:
        answer.append(mm)

answer.sort()

print(len(answer))

print(''.join(answer), end = '')
'''

'''시도1
n = int(input())

word_list = []
cnt = n

for _ in range(n):
    array = list(input())
    eng = [array[0]]

    for i in range(1,len(array)):
        
        if array[i] not in eng:
            eng.append(i)
            continue
        if array[i] in eng and array[i] == array[i-1]:
            continue
        
        cnt-=1
        
print(cnt)
'''
