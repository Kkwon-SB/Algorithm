# n개의 최소공배수를 구하는 방법
def solution(arr):                         
    answer = arr[0]                               

    for num in arr:                                 
        gcd = lambda a, b: a if not b else gcd(b, a%b)
        answer = answer*num // gcd(answer, num)     

    return answer
