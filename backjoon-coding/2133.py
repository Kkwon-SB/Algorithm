# 점화식 사용

import sys
num =  int(sys.stdin.readline())

arr = [0]*(num+1)
arr[0] = 1

for i in range(2, num+1, 2):
    arr[i] = arr[i-2] * 3
    for j in range(0, i-2, 2):
        arr[i] += arr[j] * 2

print(arr[num])