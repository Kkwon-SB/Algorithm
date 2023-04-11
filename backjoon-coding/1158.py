#요세푸스 문제 https://www.acmicpc.net/problem/1158

n, k = map(int, input().split())
array = [i for i in range(1,n+1)]
answer = []

term = k-1
print('<', end='')
while array:
    if len(array) == 1: #하나 남은 경우, 종료
        print(array.pop(-1), end='>')
        break

    if term < len(array): #기준 값이 더 작은 경우, 그대로 진행
        print(array.pop(term), end=', ')
    else:
        term = term % len(array) # 더큰 경우 순회 효과를 내기 위해 나머지 값으로
        print(array.pop(term), end=', ')

    term += (k-1)
