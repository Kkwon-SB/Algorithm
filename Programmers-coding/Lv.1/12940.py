#https://school.programmers.co.kr/learn/courses/30/lessons/12940\
#최대공약수와 최소공배수
: 이와 같은 코드로 GCD LCM문제에 접근한다면 두 수의 경우 뿐만 아니라 3개 ,4개도 가능할 것이다.

def solution(a, b):
    answer = []
    #최대공약수
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0:
            answer.append(i)
            break

    #최소공배수
    for j in range(max(a,b), a*b+1, max(a,b)):
        if j%a==0 and j%b==0:
            answer.append(j)
            break

    return answer
    
''' 
#처음 시도했던 방법 : 테스트 문제를 풀 수는 있었지만 아주 비효율적이고, 모든 케이스의 문제를 통과하지도 못했다.

def solution(n, m):
    answer = []
    max = n if n > m else m
    min = n if m > n else m    
    #최대 공약수 , 작은 수의 약수를 먼저 구하고 큰 수 부터 비교하면서 찾기 
    yak_list = [1]
    for i in range(2, int(min/2)+2):
        if min % i == 0:
            yak_list.append(i)
    yak_list.append(min)
    yak_list.sort(reverse=True)

    for i in yak_list:
        if max % i == 0:
            answer.append(i)
            break
    
    #최소공배수
    for i in range(min*2, (max * min+1), min): #(min*2, (max * min+1), min)
        if max == i:
            answer.append(i)
            break
        elif max < i:
            max+=max
        else:
            continue
    if len(answer) < 2:
        answer.append(m*n) 



    return answer
'''
