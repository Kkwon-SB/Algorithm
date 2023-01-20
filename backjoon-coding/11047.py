#https://www.acmicpc.net/problem/11047
#동전 0
#사전계획 4분  #작성8분 #수정6분

n, money = map(int, input().split())

m_list = []
answer = 0

for _ in range(n):
    m_list.append(int(input()))

for i in range(n-1, -1, -1):
    if (money // m_list[i]) > 0:
        answer = answer + (money // m_list[i])
        money -= (money // m_list[i]) * m_list[i]

print(answer)
