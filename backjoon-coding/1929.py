#https://www.acmicpc.net/problem/1929
#소수 구하기 , 에라토스테네스의 체

m , n = map(int, input().split())

A = [0] * (n + 1)

for i in range(2, n+1):
    A[i] = i

for i in range(2, int(n**0.5)+1):#배수로 소수 아닌 값 찾기
    if A[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        A[j] = 0

for i in range(m, len(A)):
    if A[i] != 0:
        print(i)
        
        
#2차 풀이
m, n = map(int, input().split())

A = [0] * (n+1)

for i in range(2, n+1):
    A[i] = i

for i in range(2, int(n**(0.5))+1):
    for j in range(i+i, n+1, i):
        if A[j] == j:#불필요
            A[j] = 0

for i in range(m,n+1):
    if A[i]:
        print(A[i])
        
#예시
m , n = map(int, input().split())

A = [i for i in range(n+1)]
A[1] = 0


for i in range(2, int(n**0.5)+1):#배수로 소수 아닌 값 찾기
    if A[i] == 0:
        continue
    for j in range(i+i, n+1, i):
        A[j] = 0

for i in range(m, len(A)):
    if A[i] != 0:
        print(i)

 
