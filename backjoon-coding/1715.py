#https://www.acmicpc.net/problem/1715
#카드 정렬하기 1715

from queue import PriorityQueue
pq = PriorityQueue()
data1 = 0
data2 = 0
answer = 0

n = int(input())

for _ in range(n):
    pq.put(int(input()))

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    answer += data1 + data2 
    pq.put(data1 + data2)

print(answer)
