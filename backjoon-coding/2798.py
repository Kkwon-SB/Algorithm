n, m = list(map(int, input().split(' '))) # 장 수, 최대 합계 수
data = list(map(int, input().split(' '))) # 카드에 적힌 숫자

#완전 탐색으로 답을 찾아도 문제 없음, 왜? 경우의 수가 적어서 - 그럼 어느정도 넘어가면 고려 상황?
# 경우의 수는 n(n-1)(n-2) / 3!

result = 0
answer = []

for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            sum_v = data[i] + data[j] + data[k]
            if sum_v <= m:
                result = max(sum_v, result)
                
print(result)

#응용 - 주어진 합이 되는 경우의 수를 가져오는 방법
'''
n, m = list(map(int, input().split(' '))) # 장 수, 최대 합계 수
data = list(map(int, input().split(' '))) # 카드에 적힌 숫자

result = 0
answer = []

for i in range(0, len(data)):
    for j in range(i+1, len(data)):
        for k in range(j+1, len(data)):
            if m == data[i] + data[j] + data[k]:
                answer += [[data[i],data[j],data[k]]]
                
print(answer)
'''