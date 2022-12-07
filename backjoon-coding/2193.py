#이친수
'''
n
1 - 1
2 - 10
3 - 101, 100
4 - 1010, 1001, 1000
5 - 10101, 10100, 10010, 10001, 10000
n이 4일때를 보자. 우선 맨 처음은 1로 시작하고, 연속될 수 없으니 다음은 0이와서 10으로 시작한다.

10뒤에 10, 01, 00이 있는데 이는 n - 2(n = 2)의 10, n - 1(n = 3)의 1뒤에 01, 00이 오게 되는 것이다.

n이 5일때도 마찬가지이다.

10 뒤에 101, 100, 010, 001, 000이 오게되는데 이는 n - 2(n = 3)일때의 101, 100과

n - 1(n = 4)일때의 1뒤의 숫자 010, 001, 000이 오게 된다.

그래서 n의 개수는 n - 2 + n - 1이 된다.
'''

from sys import stdin
num = int(stdin.readline())

arr = [1,1]

for i in range(2,num):
    arr.append(arr[i-1] + arr[i-2])

print(arr[num-1])
