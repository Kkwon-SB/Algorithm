##멀쩡한 사각형

# math를 사용한 최대공약수 구하기
import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))


# for if문을 사용한 최대공약수 구하기
def solution(w, h):
    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            return w * h - (w + h - i)
