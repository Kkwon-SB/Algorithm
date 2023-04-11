#괄호 https://www.acmicpc.net/problem/9012

test_num = int(input())
array = []

for _ in range(test_num):
    row = list(input())
    array.append(row)

def check(array):
    life = 0

    for i in array:
        if life < 0:
            return print('NO')
        if i == '(':
            life += 1
            continue
        if i == ')':
            life -= 1
            continue

    if life == 0:
        return print('YES')
    else:
        return print('NO')

for per_array in array:
    check(per_array)  
