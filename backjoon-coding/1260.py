#https://www.acmicpc.net/problem/1260
#DFS와 BFS

from collections import deque

n, m, start = map(int, input().split())
A = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    A[a].append(b)    #양방향이라 서로 넣어줌
    A[b].append(a)

for i in range(1, len(A)):#인접 리스트 오름차순으로 요소 정리
    A[i].sort()

#DFS
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    print(v, end=' ')
    for i in A[v]:    #인접 리스트 순회 
        if not visited[i]:
            DFS(i)

DFS(start)# 1 2 4 3

print()

#BFS
visited = [False] * (n+1)
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in A[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
BFS(start)
