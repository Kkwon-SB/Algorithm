# 소수 찾기.
inp_num = input()
numbers = list(map(int, input().split()))
numbers = [i for i in numbers if i > 1]  # 자연수 중 0,1 제거
cnt = 0

for num in numbers:
    err = False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            err = True  # 소수가 아님
    if err == True:
        cnt += 1

print(len(numbers) - cnt)
