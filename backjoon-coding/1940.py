'''
정렬, 투 포인트 알고리즘 이용 
- 리스트 정렬 후 리스트의 맨 앞과 뒤에서 기준 값을 비교하며 한칸 씩 이동
O(nlogn)
'''

#https://www.acmicpc.net/problem/1940
#주몽

materials  = int(input())
std  = int(input())
m_list  = list(map(int, input().split()))

start_idx = 0
end_idx = len(m_list)-1 # materials 가능
cnt = 0

m_list.sort()

while start_idx < end_idx:
    if std > m_list[start_idx] + m_list[end_idx]:
        start_idx += 1
    
    elif std < m_list[start_idx] + m_list[end_idx]:
        end_idx -=1

    else:
        cnt += 1
        start_idx += 1
        end_idx -=1
print(cnt)
