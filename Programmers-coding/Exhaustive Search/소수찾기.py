from itertools import permutations

def is_prime(n): #소수 가려내기
    
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True

def solution(numbers):
    cases = set()
    numbers = list(numbers)
    count = 0

    for i in range(1, len(numbers)+1): #1 ~ 전체 길이만큼 경우의 수 만들기 
        for x in list(permutations(numbers, i)):
            cases.add(int(''.join(str(e) for e in x)))

    for n in cases:
        if is_prime(n):
            count += 1
    return count
