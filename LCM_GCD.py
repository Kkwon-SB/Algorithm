#최대 공약수와 최소공배수 #유클리드 호제법

n , m =  35, 20
# a, b = n, m
v = n * m
while m:
    n, m = m, n % m
print('최대 공약수GCD : ',n)

print('최소 공배수LCM : ', v//2) #기존 n * m / LCM
