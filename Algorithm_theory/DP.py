#피보나치 수열 #Top - Down방식
memo = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if memo[x] != 0: #방문했던 경우가 있을 때
        return memo[x]

    memo[x] = fibo(x-1) + fibo(x-2)

    return memo[x]

print(fibo(6))
