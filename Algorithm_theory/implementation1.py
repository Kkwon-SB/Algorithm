#구현 - 상하좌우 11분

size = int(input())
now = [1,1]
moves = list(input().split())

for move in moves:
    if move == 'L':
        if now[1] >= 2:
            now[1] -= 1
    elif move == 'R':
        if now[1] <= size - 1:
            now[1] += 1
    elif move == 'U':
        if now[0] >= 2:
            now[0] -= 1
    elif move == 'D':
        if now[0] <= size - 1:
            now[0] += 1

print(now)
