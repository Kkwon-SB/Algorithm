#https://www.acmicpc.net/problem/1427
#소프트인사이드

num_list = list(map(int,input()))

for i in range(len(num_list)):
    for j in range(1, len(num_list)-i):
        if num_list[j-1] < num_list[j]: #앞에 요소가 작은 경우
            temp = num_list[j-1]
            num_list[j-1] = num_list[j]
            num_list[j] = temp

print(''.join(map(str, num_list)))

'''
import sys
print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    max = i
    for j in range(i+1, len(A)):
        if A[j] > A[max]:
            max = j
    if A[i] < A[max]:
        temp = A[i]
        A[i] = A[max]
        A[max] = temp

for i in range(len(A)):
    print(A[i])

'''
