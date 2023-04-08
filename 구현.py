#구현 - 상하좌우   이해1분, 풀이 10분

size = int(input())
orders = list(input().split())
location = [1,1]

for order in orders:
    if order == 'R' and location[1] < 5:
        location[1] += 1
        continue
    if order == 'L' and location[1] > 1:
        location[1] -= 1
        continue
    if order == 'U' and location[0] > 1:
        location[0] -= 1
        continue
    if order == 'D' and location[0] < 5:
        location[0] += 1
        continue
print(location)
