#https://www.acmicpc.net/problem/1712
#손익분기점 

a, b, c = list(map(int, input().split()))

if b >= c:
    print(-1)
else:
    print((a // (c-b))+1)
