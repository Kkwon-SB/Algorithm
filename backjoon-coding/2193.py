#이친수
'''
n
1 - 1
2 - 10
3 - 101, 100
4 - 1010, 1001, 1000
5 - 10101, 10100, 10010, 10001, 10000
n이 4일때를 보자. 우선 맨 처음은 1로 시작하고, 연속될 수 없으니 다음은 0이와서 10으로 시작한다.
'''

from sys import stdin
num = int(stdin.readline())

arr = [1,1]

for i in range(2,num):
    arr.append(arr[i-1] + arr[i-2])

print(arr[num-1])
