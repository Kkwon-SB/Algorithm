'''
sort함수를 이용하면 가장 쉽고 효율적으로 작성 가능
정렬을 직접 구현해 보자

'''
#https://www.acmicpc.net/problem/2750
#수 정렬하기


num_case = int(input())
num_list = []

for _ in range(num_case):
    num_list.append(int(input()))

for i in range(num_case):
    for j in range(1, num_case-i):
        if num_list[j-1] > num_list[j]:
            temp = num_list[j-1]
            num_list[j-1] = num_list[j]
            num_list[j] = temp
            
for i in num_list:
    print(i)
    
    
'''#sort함수를 이용한 가장 쉬운 방법
a = int(input())
b = []

for _ in range(a):
    s = int(input())
    b.append(s)

b.sort()
for i in b:
    print(i)
'''
