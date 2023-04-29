#큰 수의 법칙, 이해 3분 풀이15분
sum = 0
n, m, k =  map(int, input().split())
num_list = list(map(int, input().split()))

first = max(num_list)
num_list.remove(first)
second = max(num_list)

#num_list.sort() -> -1, -2

while m:
    for _ in range(k):
        if m == 0:
            break
        sum += first
        m -= 1

    if m != 0:
        sum += second
        m -= 1
    else:
        break

print(sum)

