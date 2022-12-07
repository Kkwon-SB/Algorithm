from sys import stdin
num = int(stdin.readline())

arr = [1,1]

for i in range(2,num):
    arr.append(arr[i-1] + arr[i-2])

print(arr[num-1])